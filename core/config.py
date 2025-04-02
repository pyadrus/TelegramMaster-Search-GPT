# -*- coding: utf-8 -*-
import configparser


def read_config_file():
    """
    Чтение данных из config.ini

    Функция считывает данные из файла конфигурации 'config.ini', который находится в директории 'user_data'.
    Файл конфигурации должен быть в кодировке 'utf-8'.

    :return: Объект ConfigParser, содержащий данные из файла конфигурации.
    """
    config = configparser.ConfigParser()
    config.read('user_data/config.ini', encoding='utf-8')
    return config


config = read_config_file()  # Чтение конфигурации из config.ini
api_id = config['telegram_settings']['api_id']
api_hash = config['telegram_settings']['api_hash']
username = config['telegram_settings']['username']
selectedmodel = config['Settings']['selectedmodel']
number_of_groups = config['ai']['number_of_groups']
program_version = config['program_version']['program_version']
date_of_program_change = config['date_of_program_change']['date_of_program_change']

program_name = config['program_name']['program_name']

GROQ_API_KEY = config['API_Groq']['GROQ_API_KEY']

proxy_user = config['proxy_data']['user']
proxy_password = config['proxy_data']['password']
proxy_port = config['proxy_data']['port']
proxy_ip = config['proxy_data']['ip']

language = config['localization']['language']
