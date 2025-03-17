# -*- coding: utf-8 -*-
import sqlite3

import openpyxl

from core.database import path_database


async def getting_data_from_database():
    """Получение данных из базы данных."""
    with sqlite3.connect(path_database) as conn:
        cursor = conn.cursor()
        # Получение всех групп из таблицы groups
        cursor.execute("SELECT * FROM groups")
        # Сохранение изменений и закрытие соединения
        data = cursor.fetchall()

    # Создание новой рабочей книги
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Chat list"
    # Заголовки столбцов
    headers = ["id", "title", "participants_count", "username", "access_hash", "date"]
    sheet.append(headers)
    # Запись данных
    for row in data:
        sheet.append(row)
    # Сохранение файла
    workbook.save("user_data/groups.xlsx")


if __name__ == '__main__':
    getting_data_from_database()