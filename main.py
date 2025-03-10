# -*- coding: utf-8 -*-
import asyncio

from loguru import logger

from ai_list import select_and_save_model
from proxy_config import setup_proxy
from telegram import search_and_save_telegram_groups

setup_proxy()  # Установка прокси

logger.add('log/log.log')


async def main():
    """
    Основная функция, выполняющая поиск по ключевым словам
    и сохранение найденных групп/каналов в базу данных.
    """

    print("1 - перебор данных\n"
          "2 - настройки")
    user_imput = input("Выберите действие: ")
    if user_imput == "1":
        await search_and_save_telegram_groups()
    elif user_imput == "2":
        print("Настройки")
        # Вызов функции
        await select_and_save_model()
    else:
        print("Некорректный ввод")


if __name__ == '__main__':
    asyncio.run(main())
