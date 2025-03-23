# -*- coding: utf-8 -*-
import openpyxl

from core.database import get_all_groups


async def getting_data_from_database():
    """Получение данных из базы данных."""
    data = get_all_groups()

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
