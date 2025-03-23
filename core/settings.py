# -*- coding: utf-8 -*-
from loguru import logger
from rich import print

from core.config import read_config_file
from core.file_utils import saving_changes_in_config_ini


async def select_and_save_model(section, option, choice):
    try:
        ai_list = {
            '1': 'qwen-2.5-32b',
            '2': 'qwen-2.5-coder-32b',
            '3': 'qwen-qwq-32b',
            '4': 'deepseek-r1-distill-qwen-32b',
            '5': 'deepseek-r1-distill-llama-70b',
            '6': 'gemma2-9b-it',
            '7': 'llama-3.1-8b-instant',
            '8': 'llama-3.2-11b-vision-preview',
            '9': 'llama-3.2-1b-preview',
            '10': 'llama-3.2-3b-preview',
            '11': 'llama-3.2-90b-vision-preview',
            '12': 'llama-3.3-70b-specdec',
            '13': 'llama-3.3-70b-versatile',
            '14': 'llama-guard-3-8b',
            '15': 'llama3-70b-8192',
            '16': 'llama3-8b-8192',
            '17': 'mistral-saba-24b',
            '18': 'mixtral-8x7b-32768',
        }

        # Вывод списка моделей
        print("Выберите модель ИИ:")
        for key, value in ai_list.items():
            print(f"{key}: {value}")
        if choice in ai_list:
            value = ai_list[choice]

            await update_config_value(section, option, value)

        else:
            print("Ошибка: некорректный выбор.")
    except Exception as e:
        logger.exception(e)


async def update_config_value(section, option, value):
    """Ввод количества вариаций названий групп, предложенных искусственным интеллектом"""
    config = await read_config_file()
    # Обновляем или добавляем секцию ai
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, value)
    # Сохранение изменений в config.ini
    await saving_changes_in_config_ini(config)
