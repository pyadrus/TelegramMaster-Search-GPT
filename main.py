# -*- coding: utf-8 -*-
import asyncio

from loguru import logger
from rich import print

from core.ai_list import select_and_save_model
from core.telegram import search_and_save_telegram_groups

logger.add('user_data/log/log.log')


async def main():
    """
    Основная функция, выполняющая поиск по ключевым словам и сохранение найденных групп/каналов в базу данных.
    """
    try:
        print("[red] TelegramMaster-Search-GPT\n\n"
              "[green] 1 - перебор данных\n"
              "[green] 2 - настройки")
        user_imput = input("Выберите действие: ")
        if user_imput == "1":
            await search_and_save_telegram_groups()
        elif user_imput == "2":
            print("[red] Настройки")
            # Вызов функции
            await select_and_save_model()
        else:
            print("[red] Некорректный ввод")
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    asyncio.run(main())
