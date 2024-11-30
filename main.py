# -*- coding: utf-8 -*-
from telethon.sync import TelegramClient, functions
import configparser

from database.database import save_to_database

config = configparser.ConfigParser()
config.read('config.ini')
api_id = config['telegram_settings']['api_id']
api_hash = config['telegram_settings']['api_hash']
username = config['telegram_settings']['username']

client = TelegramClient(username, int(api_id), api_hash)


def main():
    client.connect()
    grup_set = set()

    with open('words_list.txt', 'r', encoding='utf-8') as file:  # Открываем файл со списком слов
        list_search = file.readlines()  # Преобразуем файл в список строк

    # Удаляем символы новой строки и пробельные символы с обеих сторон строк и оставляем только строки, которые не пусты после этого
    list_search = [line.strip() for line in list_search if line.strip()]
    print(list_search)
    for search in list_search:
        result = client(functions.contacts.SearchRequest(
            q=search,
            limit=100
        ))
        for chat in result.chats:
            res = (chat.id,  # ID группы / канала
                   chat.title,  # Название группы / канала
                   chat.participants_count,  # Количество участников группы / канала
                   chat.username,  # Username группы / канала
                   chat.access_hash,  # Hash группы / канала
                   chat.date)  # Дата создания группы / канала

            grup_set.add(res)

    # Преобразование set обратно в список, если это необходимо
    grup_list = list(grup_set)

    for i in grup_list:
        print(i)

        # Сохранение данных в базу данных SQLite
        save_to_database(i)


if __name__ == '__main__':
    main()
