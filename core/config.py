# -*- coding: utf-8 -*-
import configparser

# Чтение конфигурации из config.ini
config = configparser.ConfigParser()
config.read('user_data/config.ini')
api_id = config['telegram_settings']['api_id']
api_hash = config['telegram_settings']['api_hash']
username = config['telegram_settings']['username']
selectedmodel = config['Settings']['selectedmodel']
number_of_groups = config['ai']['number_of_groups']
program_version = config['program_version']['program_version']
date_of_program_change = config['date_of_program_change']['date_of_program_change']

GROQ_API_KEY = config['API_Groq']['GROQ_API_KEY']

proxy_user = config['proxy_data']['user']
proxy_password = config['proxy_data']['password']
proxy_port = config['proxy_data']['port']
proxy_ip = config['proxy_data']['ip']
