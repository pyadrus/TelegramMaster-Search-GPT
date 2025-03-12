import configparser

from loguru import logger
from rich import print


async def saving_changes_in_config_ini(config):
    """Сохранение изменений в config.ini"""
    with open('user_data/config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)


async def read_config_file():
    """
    Чтение данных из config.ini

    Функция считывает данные из файла конфигурации 'config.ini', который находится в директории 'user_data'.
    Файл конфигурации должен быть в кодировке 'utf-8'.

    :return: Объект ConfigParser, содержащий данные из файла конфигурации.
    """
    config = configparser.ConfigParser()
    config.read('user_data/config.ini', encoding='utf-8')
    return config


async def the_api_hash_entry():
    """Запись api_hash в config.ini"""
    config = await read_config_file()
    # Получение ввода от пользователя
    api_hash = input("Введите api_hash: ").strip()
    # Обновляем или добавляем секцию telegram_settings
    if not config.has_section('telegram_settings'):
        config.add_section('telegram_settings')
    config.set('telegram_settings', 'api_hash', api_hash)
    # Сохранение изменений в config.ini
    await saving_changes_in_config_ini(config)
    print(f"api_hash {api_hash} успешно сохранен в config.ini")


async def the_api_id_entry():
    """Запись api_id в config.ini"""
    config = await read_config_file()
    # Получение ввода от пользователя
    api_id = input("Введите api_id: ").strip()
    # Обновляем или добавляем секцию telegram_settings
    if not config.has_section('telegram_settings'):
        config.add_section('telegram_settings')
    config.set('telegram_settings', 'api_id', api_id)
    # Сохранение изменений в config.ini
    await saving_changes_in_config_ini(config)
    print(f"api_id {api_id} успешно сохранен в config.ini")


async def select_and_save_model():
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

        config = await read_config_file()
        # Вывод списка моделей
        print("Выберите модель ИИ:")
        for key, value in ai_list.items():
            print(f"{key}: {value}")
        # Получение ввода от пользователя
        choice = input("Введите номер модели: ").strip()
        if choice in ai_list:
            selected_model = ai_list[choice]
            # Обновляем или добавляем секцию Settings
            if not config.has_section('Settings'):
                config.add_section('Settings')
            config.set('Settings', 'selectedmodel', selected_model)
            # Сохранение изменений в config.ini
            await saving_changes_in_config_ini(config)
            print(f"Модель {selected_model} успешно сохранена в config.ini")
        else:
            print("Ошибка: некорректный выбор.")
    except Exception as e:
        logger.exception(e)
