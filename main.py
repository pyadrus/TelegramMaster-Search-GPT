# -*- coding: utf-8 -*-
import asyncio
import os
import webbrowser

from loguru import logger
from rich import print

from core.file_utils import save_language, load_language
from core.settings import select_and_save_model, the_api_id_entry, the_api_hash_entry, number_suggested_ai_groups
from core.telegram import search_and_save_telegram_groups
from core.localization import set_language, get_text

logger.add('user_data/log/log.log')


async def change_language():
    """Функция для смены языка"""
    print(f"[yellow]{get_text('select_language')}:")
    print("[green]1 - English\n[green]2 - Русский")
    lang_choice = input("Enter choice (1 or 2): ").strip()
    if lang_choice == "1":
        set_language("en")
        save_language("en")
        print(f"[green]{get_text('language_changed')}")  # Добавьте ключ "language_changed"
    elif lang_choice == "2":
        set_language("ru")
        save_language("ru")
        print(f"[green]{get_text('language_changed')}")
    else:
        print(f"[red]{get_text('invalid_language_choice')}")


async def main():
    """
    Основная функция, выполняющая поиск по ключевым словам и сохранение найденных групп/каналов в базу данных.
    """
    try:
        # Загружаем сохранённый язык или запрашиваем при первом запуске
        if not os.path.exists("user_data/lang_settings.json"):
            print("[yellow]First launch detected / Обнаружен первый запуск")
            print(f"[yellow]{get_text('select_language')}:")
            print("[green]1 - English\n[green]2 - Русский")
            lang_choice = input("Enter choice (1 or 2): ").strip()
            if lang_choice == "1":
                set_language("en")
                save_language("en")
            elif lang_choice == "2":
                set_language("ru")
                save_language("ru")
            else:
                set_language("ru")  # По умолчанию русский
                save_language("ru")
                print(f"[red]{get_text('invalid_language_choice')}")
        else:
            current_language = load_language()
            set_language(current_language)

        # Основное меню
        while True:  # Добавляем цикл для возврата в меню
            print(f"[red] {get_text('title')}\n\n"
                  f"[green] {get_text('menu_1')}\n"
                  f"[green] {get_text('menu_2')}\n"
                  f"[green] {get_text('menu_3')}\n")
            user_input = input(get_text("select_action"))

            if user_input == "1":  # Добавляем пункт меню для поиска по ключевым словам
                messages_for_ai = input("Введите сообщение для ИИ: ")
                await search_and_save_telegram_groups(user_input=messages_for_ai)
            elif user_input == "2":  # Добавляем пункт меню для настроек
                print(f"[red] {get_text('settings_title')}\n\n"
                      f"[green] {get_text('settings_1')}\n"
                      f"[green] {get_text('settings_2')}\n"
                      f"[green] {get_text('settings_3')}\n"
                      f"[green] {get_text('settings_4')}\n"
                      f"[green] {get_text('settings_5')}\n")  # Новый пункт меню
                user_input = input(get_text("select_action"))
                if user_input == "1":  # Добавляем пункт меню для выбора модели
                    print(f"[red] {get_text('ai_model_select')}")
                    choice = input("Введите номер модели: ").strip()
                    await select_and_save_model(choice=choice)
                elif user_input == "2":  # Добавляем пункт меню для ввода API_ID
                    print(f"[red] {get_text('api_id_entry')}")
                    api_id = input("Введите api_id: ").strip()
                    await the_api_id_entry(api_id=api_id)
                elif user_input == "3":  # Добавляем пункт меню для ввода API_HASH
                    print(f"[red] {get_text('api_hash_entry')}")
                    api_hash = input("Введите api_hash: ").strip()
                    await the_api_hash_entry(api_hash=api_hash)
                elif user_input == "4":  # Добавляем пункт меню для смены языка
                    await change_language()
                elif user_input == "5":  # Добавляем пункт ввода количества наименований групп, предложенных ИИ
                    number_of_groups = input("Введите количество вариаций названий групп, предложенных искусственным интеллектом: ").strip()
                    await number_suggested_ai_groups(number_of_groups=number_of_groups)
            elif user_input == "3":  # Добавляем пункт меню для открытия документации
                print(f"[red] {get_text('docs_open')}\n")
                webbrowser.open('https://github.com/pyadrus/TelegramMaster-Search-GPT/wiki', new=2)
            else:
                print(f"[red] {get_text('invalid_input')}")
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    asyncio.run(main())
