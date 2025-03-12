# -*- coding: utf-8 -*-
import asyncio
import webbrowser

from loguru import logger
from rich import print

from core.settings.settings import select_and_save_model, the_api_id_entry, the_api_hash_entry
from core.telegram import search_and_save_telegram_groups

logger.add('user_data/log/log.log')


async def main():
    """
    Основная функция, выполняющая поиск по ключевым словам и сохранение найденных групп/каналов в базу данных.
    """
    try:
        print("[red] TelegramMaster-Search-GPT\n\n"

              "[green] 1 - Перебор данных\n"
              "[green] 2 - Настройки\n"
              "[green] 3 - Документация\n")
        user_input = input("Выберите действие: ")
        if user_input == "1":
            await search_and_save_telegram_groups()
        elif user_input == "2":
            print("[red] Настройки\n\n"

                  "[green] 1 - выбор модели ИИ\n"
                  "[green] 2 - запись api_id\n"
                  "[green] 3 - запись api_hash\n")
            user_input = input("Выберите действие: ")
            if user_input == "1":  # выбор модели ИИ
                print("[red] Выбор модели ИИ")
                # Вызов функции
                await select_and_save_model()
            elif user_input == "2":  # запись api_id
                print("[red] Запись api_id")
                await the_api_id_entry()
            elif user_input == "3":  # запись api_hash
                print("[red] Запись api_hash")
                await the_api_hash_entry()
        elif user_input == "3":
            print("[red] Открыть документацию\n")
            webbrowser.open(
                'https://github.com/pyadrus/TelegramMaster-Search-GPT/wiki/Руководство-по-работе-с-TelegramMaster‐Search‐GPT',
                new=2)

        else:
            print("[red] Некорректный ввод")
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    asyncio.run(main())
