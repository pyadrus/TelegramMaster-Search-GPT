# -*- coding: utf-8 -*-
from telethon.sync import TelegramClient, functions
import configparser
import sqlite3

config = configparser.ConfigParser()
config.read('config.ini')
api_id = config['telegram_settings']['api_id']
api_hash = config['telegram_settings']['api_hash']
username = config['telegram_settings']['username']

client = TelegramClient(username, int(api_id), api_hash)


def save_to_database(data_tuple):
    # Подключение к базе данных
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    # Создание таблицы, если её нет
    cursor.execute('''CREATE TABLE IF NOT EXISTS groups (id, title, participants_count, username, access_hash, date)''')
    # Вставка данных в таблицу
    cursor.execute(
        '''INSERT INTO groups (id, title, participants_count, username, access_hash, date) VALUES (?, ?, ?, ?, ?, ?) ''',
        data_tuple)
    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()


def main():
    client.connect()
    grup_set = set()
    list_search = ['linux', 'Линукс', 'Ubuntu', 'Debian', 'Fedora', 'ArchLinux', 'CentOS', 'Kali Linux', 'Bash',
                   'Shell', 'Kernel', 'Systemd', 'Open Source', 'GNU/Linux', 'Terminal', 'Command Line', 'Sysadmin',
                   'DevOps', 'Server Administration', 'Linux Academy', 'Linux Education', 'Linux Users',
                   'Linux Community', 'Linux News', 'Linux Development', 'Linux Gaming', 'Embedded Linux',
                   'Raspberry Pi', 'Docker', 'Kubernetes', 'System Administration', 'Linux Mint', 'Elementary OS',
                   'LXDE', 'XFCE']
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
