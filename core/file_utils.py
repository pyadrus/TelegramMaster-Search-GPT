# -*- coding: utf-8 -*-
import json
import os


async def writing_file(ai_response) -> None:
    """Запись содержимого в файл words_list.txt."""
    with open('user_data/words_list.txt', 'w', encoding='utf-8') as file:
        file.write(ai_response)


async def reading_file() -> list[str]:
    """Чтение поисковых терминов из файла words_list.txt."""
    with open('user_data/words_list.txt', 'r', encoding='utf-8') as file:
        search_terms = file.readlines()
    return search_terms


def load_language():
    """Функция загрузки языка из файла"""
    try:
        with open("user_data/lang_settings.json", "r") as f:
            return json.load(f).get("language", "ru")
    except FileNotFoundError:
        return "ru"  # По умолчанию русский, если файла нет


def save_language(lang):
    """Функция сохранения языка в файл"""
    os.makedirs("user_data", exist_ok=True)  # Создаём папку, если её нет
    with open("user_data/lang_settings.json", "w") as f:
        json.dump({"language": lang}, f)


async def saving_changes_in_config_ini(config):
    """Сохранение изменений в config.ini"""
    with open('user_data/config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)
