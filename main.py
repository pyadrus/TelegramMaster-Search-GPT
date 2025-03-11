# -*- coding: utf-8 -*-
import asyncio

from loguru import logger
from rich import print

from core.ai_list import select_and_save_model, the_api_id_entry
from core.telegram import search_and_save_telegram_groups

logger.add('user_data/log/log.log')


async def main():
    """
    Основная функция, выполняющая поиск по ключевым словам и сохранение найденных групп/каналов в базу данных.
    """
    try:
        print("[red] TelegramMaster-Search-GPT\n\n"
              
              "[green] 1 - Перебор данных\n"
              "[green] 2 - Настройки")
        user_input = input("Выберите действие: ")
        if user_input == "1":
            await search_and_save_telegram_groups()
        elif user_input == "2":
            print("[red] Настройки\n\n"
                  "[green] 1 - выбор модели ИИ\n"
                  "[green] 2 - запись api_id")
            user_input = input("Выберите действие: ")
            if user_input == "1":
                print("Выбор модели ИИ")
                # Вызов функции
                await select_and_save_model()
            elif user_input == "2":
                print("Запись api_id")
                await the_api_id_entry()
        else:
            print("[red] Некорректный ввод")
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    asyncio.run(main())
