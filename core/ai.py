# -*- coding: utf-8 -*-
import os

from groq import AsyncGroq
from loguru import logger

from core.config import selectedmodel, number_of_groups, GROQ_API_KEY
from core.file_utils import load_language
from core.localization import get_text
from core.localization import set_language
from core.proxy_config import setup_proxy


def promt_ai(number_of_groups, user_input):
    """Промт для AI"""
    # Используем get_text для получения переведённого текста промта
    promt_ai = f"""{get_text('ai_prompt')} {number_of_groups} {get_text('ai_prompt_unique_keywords')} 
    {get_text('ai_prompt_based_on')} {user_input}. {get_text('ai_prompt_return_format')}"""
    return promt_ai


async def get_groq_response(user_input):
    """Получение ответа от Groq API."""

    # Загружаем язык при запуске, если файл настроек существует
    if os.path.exists("user_data/lang_settings.json"):
        current_language = load_language()
        set_language(current_language)
    else:
        # Устанавливаем язык по умолчанию, если настройки отсутствуют
        set_language("ru")  # Можно изменить на "en" по умолчанию, если нужно

    setup_proxy()  # Установка прокси
    # Инициализация Groq клиента
    client_groq = AsyncGroq(api_key=GROQ_API_KEY)
    try:
        # Формируем запрос к Groq API
        chat_completion = await client_groq.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": promt_ai(number_of_groups, user_input)
                }
            ],
            model=f"{selectedmodel}",
        )
        # Получаем ответ от ИИ
        ai_response = chat_completion.choices[0].message.content
        return ai_response
    except Exception as e:
        logger.exception(e)
