# -*- coding: utf-8 -*-
import sqlite3

from loguru import logger

path_database = 'user_data/your_database.db'


def save_to_database(data_tuple):
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
    try:
        with sqlite3.connect(path_database) as conn:
            cursor = conn.cursor()
            # Создание временной таблицы с уникальными записями
            cursor.execute('''CREATE TEMPORARY TABLE temp_groups AS SELECT DISTINCT id, title, participants_count, 
                              username, access_hash, date FROM groups''')
            # Очистка основной таблицы
            cursor.execute('DELETE FROM groups')
            # Копирование уникальных записей обратно в основную таблицу
            cursor.execute('''INSERT INTO groups (id, title, participants_count, username, access_hash, date) SELECT 
                              id, title, participants_count, username, access_hash, date FROM temp_groups''')
            # Удаление временной таблицы
            cursor.execute('DROP TABLE temp_groups')
            # Сохранение изменений и закрытие соединения
            conn.commit()
    except Exception as e:
        logger.exception(e)
