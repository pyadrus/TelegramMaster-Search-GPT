# -*- coding: utf-8 -*-
import openpyxl

from core.database import get_all_groups


async def getting_data_from_database():
    """Получение данных из базы данных."""
    workbook = openpyxl.Workbook()  # Создание новой рабочей книги
    sheet = workbook.active
    sheet.title = "Chat list"
    # Заголовки столбцов
    headers = ["id", "title", "participants_count", "username", "access_hash", "date"]
    sheet.append(headers)
    # Запись данных
    for row in get_all_groups():
        sheet.append(row)
    # Сохранение файла
    workbook.save("user_data/groups.xlsx")


if __name__ == '__main__':
    getting_data_from_database()
