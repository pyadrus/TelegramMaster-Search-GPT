# -*- coding: utf-8 -*-
import asyncio
import webbrowser
import json
import os

from loguru import logger
from rich import print

from core.settings.settings import select_and_save_model, the_api_id_entry, the_api_hash_entry
from core.telegram import search_and_save_telegram_groups
from localization import set_language, get_text

logger.add('user_data/log/log.log')

# Функция загрузки языка из файла
def load_language():
    try:
        with open("user_data/lang_settings.json", "r") as f:
            return json.load(f).get("language", "ru")
    except FileNotFoundError:
        return "ru"  # По умолчанию русский, если файла нет

# Функция сохранения языка в файл
def save_language(lang):
    os.makedirs("user_data", exist_ok=True)  # Создаём папку, если её нет
    with open("user_data/lang_settings.json", "w") as f:
        json.dump({"language": lang}, f)

# Функция для смены языка
async def change_language():
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

            if user_input == "1":
                await search_and_save_telegram_groups()
            elif user_input == "2":
                print(f"[red] {get_text('settings_title')}\n\n"
                      f"[green] {get_text('settings_1')}\n"
                      f"[green] {get_text('settings_2')}\n"
                      f"[green] {get_text('settings_3')}\n"
                      f"[green] 4 - {get_text('change_language')}")  # Новый пункт меню
                user_input = input(get_text("select_action"))
                if user_input == "1":
                    print(f"[red] {get_text('ai_model_select')}")
                    await select_and_save_model()
                elif user_input == "2":
                    print(f"[red] {get_text('api_id_entry')}")
                    await the_api_id_entry()
                elif user_input == "3":
                    print(f"[red] {get_text('api_hash_entry')}")
                    await the_api_hash_entry()
                elif user_input == "4":
                    await change_language()
            elif user_input == "3":
                print(f"[red] {get_text('docs_open')}\n")
                webbrowser.open(
                    'https://github.com/pyadrus/TelegramMaster-Search-GPT/wiki',
                    new=2)
            else:
                print(f"[red] {get_text('invalid_input')}")
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    asyncio.run(main())