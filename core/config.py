# -*- coding: utf-8 -*-
import configparser
import os

from dotenv import load_dotenv
from loguru import logger

# Чтение конфигурации из config.ini
config = configparser.ConfigParser()
config.read('user_data/config.ini')
api_id = config['telegram_settings']['api_id']
api_hash = config['telegram_settings']['api_hash']
username = config['telegram_settings']['username']

selectedmodel = config['Settings']['selectedmodel']

# Загружаем переменные окружения из файла .env
load_dotenv()


# Функции для получения переменных окружения
def get_groq_api_key() -> str:
    """Возвращает API-ключ для Groq."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY не найден в переменных окружения.")
    return api_key


# Настройки прокси
def get_proxy_user() -> str:
    """Возвращает логин для прокси."""
    try:
        user = os.getenv("USER")
        if not user:
            raise ValueError("USER (логин прокси) не найден в переменных окружения.")
        return user
    except Exception as e:
        logger.exception(e)


def get_proxy_password() -> str:
    """Возвращает пароль для прокси."""
    try:
        password = os.getenv("PASSWORD")
        if not password:
            raise ValueError("PASSWORD (пароль прокси) не найден в переменных окружения.")
        return password
    except Exception as e:
        logger.exception(e)


def get_proxy_port() -> str:
    """Возвращает порт для прокси."""
    try:
        port = os.getenv("PORT")
        if not port:
            raise ValueError("PORT (порт прокси) не найден в переменных окружения.")
        return port
    except Exception as e:
        logger.exception(e)


def get_proxy_ip() -> str:
    """Возвращает IP для прокси."""
    try:
        ip = os.getenv("IP")
        if not ip:
            raise ValueError("IP (адрес прокси) не найден в переменных окружения.")
        return ip
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    get_groq_api_key()
    get_proxy_user()
    get_proxy_password()
    get_proxy_port()
    get_proxy_ip()
