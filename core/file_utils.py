# -*- coding: utf-8 -*-

async def writing_file(ai_response) -> None:
    """Запись содержимого в файл words_list.txt."""
    with open('user_data/words_list.txt', 'w', encoding='utf-8') as file:
        file.write(ai_response)


async def reading_file() -> list[str]:
    """Чтение поисковых терминов из файла words_list.txt."""
    with open('user_data/words_list.txt', 'r', encoding='utf-8') as file:
        search_terms = file.readlines()
    return search_terms


async def saving_changes_in_config_ini(config):
    """Сохранение изменений в config.ini"""
    with open('user_data/config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)
