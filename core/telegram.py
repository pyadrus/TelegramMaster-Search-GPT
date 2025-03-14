# -*- coding: utf-8 -*-
from loguru import logger
from rich import print
from telethon.errors import AuthKeyUnregisteredError, FloodWaitError
from telethon.sync import TelegramClient, functions

from core.ai import get_groq_response
from core.config import username, api_id, api_hash
from core.database.database import save_to_database, remove_duplicates
from core.proxy_config import setup_proxy


async def connect_to_telegram() -> TelegramClient:
    """Инициализация и подключение клиента Telegram."""
    client = TelegramClient(f"user_data/{username}", int(api_id), api_hash)
    await client.connect()  # Подключение к Telegram
    return client


async def writing_file(ai_response) -> None:
    """Запись содержимого в файл words_list.txt."""
    with open('user_data/words_list.txt', 'w', encoding='utf-8') as file:
        file.write(ai_response)


async def reading_file() -> list[str]:
    """Чтение поисковых терминов из файла words_list.txt."""
    with open('user_data/words_list.txt', 'r', encoding='utf-8') as file:
        search_terms = file.readlines()
    return search_terms


async def converting_into_a_list_for_further_processing(groups_set) -> None:
    """Преобразование множества групп в список и сохранение в базу данных."""
    groups_list = list(groups_set)
    for group in groups_list:
        save_to_database(group)  # Сохранение данных в базу данных SQLite


async def search_and_processing_found_groups(client, term, groups_set) -> None:
    """Поиск групп Telegram и обработка результатов."""
    try:
        search_results = await client(functions.contacts.SearchRequest(q=term, limit=100))
        # Обработка найденных групп и каналов
        for chat in search_results.chats:
            group_info = (
                chat.id,  # ID группы / канала
                chat.title,  # Название группы / канала
                chat.participants_count,  # Количество участников
                chat.username,  # Username группы / канала
                chat.access_hash,  # Hash группы / канала
                chat.date  # Дата создания
            )
            groups_set.add(group_info)  # Добавление информации в множество
    except AuthKeyUnregisteredError as e:
        print(f"Ошибка аккаунта: {e}")
        return
    except FloodWaitError as e:
        print(f"Ошибка флуда: {e}")
        return


async def search_and_save_telegram_groups(user_input: str) -> None:
    """Основная функция для поиска и сохранения групп Telegram."""
    try:
        setup_proxy()  # Установка прокси
        client = connect_to_telegram()  # Инициализация клиента Telegram
        groups_set = set()  # Создание множества для уникальных результатов

        # Получение ответа ИИ и его обработка
        ai_response = await get_groq_response(user_input)  # Получение ответа от Groq API.
        await writing_file(ai_response)  # Сохранение ответа ИИ в файл words_list.txt
        search_terms = await reading_file()  # Чтение списка ключевых слов из файла

        # Очистка списка от пустых строк и пробелов
        search_terms = [term.strip() for term in search_terms if term.strip()]
        logger.info("Ключевые слова для поиска:", search_terms)

        # Поиск групп по каждому термину
        for term in search_terms:
            # Поиск групп и каналов по ключевому слову
            await search_and_processing_found_groups(client, term, groups_set)

        # Обработка и сохранение результатов
        await converting_into_a_list_for_further_processing(groups_set)
        remove_duplicates()  # Удаление дубликатов из базы данных

    except Exception as e:
        logger.exception(e)
