# -*- coding: utf-8 -*-
from loguru import logger
from rich import print
from groq import AsyncGroq

from config import get_groq_api_key, selectedmodel
from proxy_config import setup_proxy

setup_proxy()  # Установка прокси

# Инициализация Groq клиента
client_groq = AsyncGroq(api_key=get_groq_api_key())


async def get_groq_response(user_input):
    """
    Получение ответа от Groq API.
    """
    try:
        # Формируем запрос к Groq API
        chat_completion = await client_groq.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Придумай 200 уникальных и интересных ключевых словосочетаний для поиска в Telegram, на "
                               f"основе текста пользователя: {user_input}. Верни результат в формате простого списка, "
                               f"каждое слово на новой строке, без нумерации и дополнительных символов.",
                }
            ],
            model=f"{selectedmodel}",
        )

        # Получаем ответ от ИИ
        ai_response = chat_completion.choices[0].message.content

        return ai_response
    except Exception as e:
        logger.exception(e)
