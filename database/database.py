# -*- coding: utf-8 -*-
import sqlite3


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
