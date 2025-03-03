# -*- coding: utf-8 -*-
"""
Скрипт для поиска групп и каналов Telegram по ключевым словам
и сохранения информации в базу данных.
"""

import asyncio
import configparser

from groq import AsyncGroq
from loguru import logger
from telethon.sync import TelegramClient, functions

from config import get_groq_api_key
from database.database import save_to_database
from proxy_config import setup_proxy

setup_proxy()  # Установка прокси

logger.add('log/log.log')

# Чтение конфигурации из config.ini
config = configparser.ConfigParser()
config.read('config.ini')
api_id = config['telegram_settings']['api_id']
api_hash = config['telegram_settings']['api_hash']
username = config['telegram_settings']['username']
# Инициализация Groq клиента
client_groq = AsyncGroq(api_key=get_groq_api_key())


async def get_groq_response(user_input):
    """
    Получение ответа от Groq API.
    """

    # Формируем запрос к Groq API
    chat_completion = await client_groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Придумай 50 уникальных и интересных ключевых словосочетаний для поиска в Telegram, на основе текста пользователя: {user_input}. Верни результат в формате простого списка, каждое слово на новой строке, без нумерации и дополнительных символов.",
            }
        ],
        model="gemma2-9b-it",
    )

    # Получаем ответ от ИИ
    ai_response = chat_completion.choices[0].message.content

    return ai_response


async def main():
    """
    Основная функция, выполняющая поиск по ключевым словам
    и сохранение найденных групп/каналов в базу данных.
    """
    # Инициализация клиента Telegram
    client = TelegramClient(username, int(api_id), api_hash)
    await client.connect()  # Подключение к Telegram
    groups_set = set()  # Создание множества для уникальных результатов

    user_input = input("Введите сообщение для ИИ: ")
    ai_response = await get_groq_response(user_input)
    print("Ответ от ИИ:", ai_response)

    # Сохранение ответа ИИ в файл words_list.txt
    with open('words_list.txt', 'w', encoding='utf-8') as file:
        file.write(ai_response)

    # Чтение списка ключевых слов из файла
    with open('words_list.txt', 'r', encoding='utf-8') as file:
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

    for group in groups_list:
        logger.info("Найденная группа/канал:", group)
        save_to_database(group)  # Сохранение данных в базу данных SQLite


if __name__ == '__main__':
    asyncio.run(main())
