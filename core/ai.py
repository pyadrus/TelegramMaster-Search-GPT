# -*- coding: utf-8 -*-
from groq import AsyncGroq
from loguru import logger
from rich import print

from core.config import selectedmodel, number_of_groups, GROQ_API_KEY
from core.proxy_config import setup_proxy


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
                    "content": f"Придумай {number_of_groups} уникальных и интересных ключевых словосочетаний для поиска в Telegram, на "
                               f"основе текста пользователя: {user_input}. Верни результат в формате простого списка, "
                               f"каждое слово на новой строке, без нумерации и дополнительных символов.",
                }
            ],
            model=f"{selectedmodel}",
        )
        # Получаем ответ от ИИ
        ai_response = chat_completion.choices[0].message.content
        print("Ответ от ИИ:", ai_response)
        return ai_response
    except Exception as e:
        logger.exception(e)
