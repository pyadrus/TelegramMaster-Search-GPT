# -*- coding: utf-8 -*-
import os
import os.path

import flet as ft
from loguru import logger
from telethon.errors import AuthKeyUnregisteredError, FloodWaitError
from telethon.sync import TelegramClient, functions

from core.ai import get_groq_response
from core.config import api_id, api_hash
from core.database import save_to_database, remove_duplicates
from core.file_utils import writing_file, reading_file
from core.localization import get_text
from core.settings import add_view_with_fields_and_button


def find_filess(directory_path, extension) -> list:
    """
    Поиск файлов с определенным расширением в директории. Расширение файла должно быть указанно без точки.

    :param directory_path: Путь к директории
    :param extension: Расширение файла (указанное без точки)
    :return list: Список имен найденных файлов
    """
    entities = []  # Создаем словарь с именами найденных аккаунтов в папке user_data/accounts
    try:
        for x in os.listdir(directory_path):
            if x.endswith(f".{extension}"):  # Проверяем, заканчивается ли имя файла на заданное расширение
                file = os.path.splitext(x)[0]  # Разделяем имя файла на имя без расширения и расширение
                entities.append(file)  # Добавляем информацию о файле в список

        logger.info(f"🔍 Найденные файлы: {entities}")  # Выводим имена найденных аккаунтов

        return entities  # Возвращаем список json файлов
    except FileNotFoundError:
        logger.error(f"❌ Ошибка! Директория {directory_path} не найдена!")

async def connect_to_telegram() -> TelegramClient:
    """Инициализация и подключение клиента Telegram."""
    for session_name in find_filess(directory_path='user_data/accounts', extension="session"):
        logger.info(f"🔑 Подключение к аккаунту: {session_name}")
        client = TelegramClient(f"user_data/accounts/{session_name}", int(api_id), api_hash)
        await client.connect()  # Подключение к Telegram
        return client


async def converting_into_a_list_for_further_processing(groups_set) -> None:
    """Преобразование множества групп в список и сохранение в базу данных."""
    for group in list(groups_set):
        save_to_database(group)  # Сохранение данных в базу данных SQLite


async def search_and_processing_found_groups(lv, page, client, term, groups_set) -> None:
    """Поиск групп Telegram и обработка результатов."""
    try:
        search_results = await client(functions.contacts.SearchRequest(q=term, limit=20))
        # Обработка найденных групп и каналов
        for chat in search_results.chats:
            # Create a tuple with all the chat information and add it as a single element
            group_data = (
                chat.id,                # ID группы / канала
                chat.title,            # Название группы / канала
                chat.participants_count, # Количество участников
                chat.username,         # Username группы / канала
                chat.access_hash,      # Hash группы / канала
                chat.date             # Дата создания
            )
            groups_set.add(group_data)  # Add the tuple to the set
    except AuthKeyUnregisteredError as e:
        await message_output_program_window(lv, page, f"{get_text('error')} {e}")
        return
    except FloodWaitError as e:
        await message_output_program_window(lv, page, f"{get_text('error_1')} {e}")
        return


async def message_output_program_window(lv: ft.ListView, page: ft.Page, message_program):
    """
    Вывод сообщений в окно программы.
    :param lv: ListView
    :param page: Страница приложения.
    :param message_program: Сообщение.
    """
    lv.controls.append(ft.Text(f"{message_program}", color=ft.colors.RED))  # отображаем сообщение в ListView
    page.update()  # Обновляем страницу


async def search_and_save_telegram_groups(page: ft.Page) -> None:
    """Основная функция для поиска и сохранения групп Telegram."""
    lv = ft.ListView(expand=10, spacing=1, padding=2, auto_scroll=True)
    page.controls.append(lv)  # добавляем ListView на страницу для отображения логов 📝
    lv.controls.append(ft.Text(get_text("text_data_processing")))  # отображаем сообщение в ListView
    messages_for_ai = ft.TextField(label=get_text("select_action_4"), multiline=True, max_lines=19)

    async def btn_click(e) -> None:
        try:
            client = await connect_to_telegram()  # Инициализация клиента Telegram
            groups_set = set()  # Создание множества для уникальных результатов

            # Получение ответа ИИ и его обработка
            ai_response = await get_groq_response(messages_for_ai.value)  # Получение ответа от Groq API.
            await message_output_program_window(lv, page, f"{get_text('ai_model_select_1')}: {ai_response}")
            await message_output_program_window(lv, page, ai_response)
            await writing_file(ai_response)  # Сохранение ответа ИИ в файл words_list.txt
            search_terms = await reading_file()  # Чтение списка ключевых слов из файла

            # Очистка списка от пустых строк и пробелов
            search_terms = [term.strip() for term in search_terms if term.strip()]

            # Поиск групп по каждому термину
            for term in search_terms:
                # Поиск групп и каналов по ключевому слову
                await search_and_processing_found_groups(lv, page, client, term, groups_set)

            # Обработка и сохранение результатов
            await converting_into_a_list_for_further_processing(groups_set)
            remove_duplicates()  # Удаление дубликатов из базы данных
            client.disconnect()  # Отключение от Telegram

            page.go("/")  # Изменение маршрута в представлении существующих настроек
            page.update()

        except Exception as e:
            logger.exception(e)

    await add_view_with_fields_and_button(page, [messages_for_ai], btn_click, lv)
