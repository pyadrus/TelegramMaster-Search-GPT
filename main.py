# -*- coding: utf-8 -*-
"""
Скрипт для поиска групп и каналов Telegram по ключевым словам
и сохранения информации в базу данных.
"""

from telethon.sync import TelegramClient, functions
import configparser
from database.database import save_to_database
from loguru import logger

logger.add('log/log.log')

# Чтение конфигурации из config.ini
config = configparser.ConfigParser()
config.read('config.ini')
api_id = config['telegram_settings']['api_id']
api_hash = config['telegram_settings']['api_hash']
username = config['telegram_settings']['username']

# Инициализация клиента Telegram
client = TelegramClient(username, int(api_id), api_hash)

def main():
    """
    Основная функция, выполняющая поиск по ключевым словам
    и сохранение найденных групп/каналов в базу данных.
    """
    client.connect()  # Подключение к Telegram
    groups_set = set()  # Создание множества для уникальных результатов

    # Чтение списка ключевых слов из файла
    with open('words_list.txt', 'r', encoding='utf-8') as file:
        search_terms = file.readlines()

    # Очистка списка от пустых строк и пробелов
    search_terms = [term.strip() for term in search_terms if term.strip()]

    logger.info("Ключевые слова для поиска:", search_terms)

    for term in search_terms:
        # Поиск групп и каналов по ключевому слову
        search_results = client(functions.contacts.SearchRequest(
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
    main()
