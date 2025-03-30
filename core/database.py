# -*- coding: utf-8 -*-
import sqlite3

from loguru import logger

path_database = 'user_data/your_database.db'


def get_all_groups():
    """Получение всех групп из базы данных."""
    # Создание подключения к базе данных
    with sqlite3.connect(path_database) as conn:
        cursor = conn.cursor()
        # Получение всех групп из таблицы groups
        cursor.execute("SELECT * FROM groups")
        # Сохранение изменений и закрытие соединения
        data = cursor.fetchall()
    return data


def save_to_database(data_tuple):
    """Запись полученных групп и каналов в базу данных"""
    try:
        with sqlite3.connect(path_database) as conn:
            cursor = conn.cursor()
            # Создание таблицы, если её нет
            cursor.execute('''CREATE TABLE IF NOT EXISTS groups (id, title, participants_count, username, access_hash, 
                              date)''')
            # Вставка данных в таблицу
            cursor.execute('''INSERT INTO groups (id, title, participants_count, username, access_hash, date) 
                                  VALUES (?, ?, ?, ?, ?, ?) ''',
                           data_tuple)
            # Сохранение изменений и закрытие соединения
            conn.commit()
    except Exception as e:
        logger.exception(e)


def remove_duplicates():
    """Удаление дубликатов в таблице groups по колонке id"""
    try:
        with sqlite3.connect(path_database) as conn:
            cursor = conn.cursor()
            # Удаляем дубликаты, оставляя запись с наименьшим rowid
            cursor.execute('''DELETE FROM groups WHERE rowid NOT IN (SELECT MIN(rowid) FROM groups GROUP BY id)''')
            conn.commit()
    except Exception as e:
        logger.exception(e)
