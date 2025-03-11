# -*- coding: utf-8 -*-

from loguru import logger
from telethon.sync import TelegramClient, functions

from core.ai import get_groq_response
from core.config import username, api_id, api_hash
from core.database.database import save_to_database, remove_duplicates
from core.proxy_config import setup_proxy


async def search_and_save_telegram_groups():
    """Поиск и сохранение групп Telegram"""

    setup_proxy()  # Установка прокси

    # Инициализация клиента Telegram
    client = TelegramClient(username, int(api_id), api_hash)
    await client.connect()  # Подключение к Telegram
    groups_set = set()  # Создание множества для уникальных результатов

    user_input = input("Введите сообщение для ИИ: ")
    ai_response = await get_groq_response(user_input)
    print("Ответ от ИИ:", ai_response)

    # Сохранение ответа ИИ в файл words_list.txt
    with open('../user_data/words_list.txt', 'w', encoding='utf-8') as file:
        file.write(ai_response)

    # Чтение списка ключевых слов из файла
    with open('../user_data/words_list.txt', 'r', encoding='utf-8') as file:
        search_terms = file.readlines()

    # Очистка списка от пустых строк и пробелов
    search_terms = [term.strip() for term in search_terms if term.strip()]

    logger.info("Ключевые слова для поиска:", search_terms)

    for term in search_terms:
        # Поиск групп и каналов по ключевому слову
        search_results = await client(functions.contacts.SearchRequest(
            q=term,
            limit=100
        ))

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

    # Преобразование множества в список для дальнейшей обработки
    groups_list = list(groups_set)
    logger.info("Найденные группы/каналы:", groups_list)

    # Удаление дубликатов из базы данных
    remove_duplicates()

    for group in groups_list:
        save_to_database(group)  # Сохранение данных в базу данных SQLite
