# -*- coding: utf-8 -*-
from groq import AsyncGroq
from loguru import logger

from core.config import selectedmodel, number_of_groups, GROQ_API_KEY
from core.localization import get_text
from core.proxy_config import setup_proxy


def promt_ai(number_of_groups, user_input) -> str:
    """Промт для AI. Используем get_text для получения переведённого текста промта"""
    return (f"{get_text('ai_prompt')} {number_of_groups} {get_text('ai_prompt_unique_keywords')} "
            f"{get_text('ai_prompt_based_on')} {user_input}. {get_text('ai_prompt_return_format')}")


async def get_groq_response(user_input):
    """Получение ответа от Groq API."""
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
        # Возвращаем ответ от ИИ
        return chat_completion.choices[0].message.content
    except Exception as e:
        logger.exception(e)
