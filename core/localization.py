# -*- coding: utf-8 -*-
translations = {
    "ru": {
        "title": "TelegramMaster-Search-GPT",

        "menu_1": "1 - Перебор данных",
        "menu_2": "2 - Настройки",
        "menu_3": "3 - Документация",
        "menu_4": "4 - Получение спарсеных данных",

        "select_action": "Выберите действие: ",
        "select_action_1": "Введите номер модели: ",
        "select_action_2": "Введите api_id: ",
        "select_action_3": "Введите api_hash: ",
        "select_action_4": "Введите количество вариаций названий групп, предложенных искусственным интеллектом: ",

        "settings_title": "Настройки",

        "settings_1": "1 - Выбор модели ИИ",
        "settings_2": "2 - Запись api_id и api_hash",
        "settings_4": "4 - Сменить язык",
        "settings_5": "5 - Сменить количество предложенных групп ИИ",

        "ai_model_select": "Выбор модели ИИ",
        "ai_model_select_1": "Ответ от ИИ:",
        "ai_model_select_2": "Выберите модель ИИ:",
        "ai_model_select_3": "Ошибка: некорректный выбор.",
        "ai_model_select_4": "Введите сообщение для ИИ: ",

        "api_id_entry": "Запись api_id",
        "api_hash_entry": "Запись api_hash",
        "docs_open": "Открыть документацию",
        "invalid_input": "Некорректный ввод",
        "select_language": "Выберите язык",
        "invalid_language_choice": "Некорректный выбор языка, используется сохранённый",
        "change_language": "Сменить язык",
        "language_changed": "Язык успешно изменён",

        "error": "Ошибка аккаунта: ",
        "error_1": "Ошибка флуда: ",

        "messages": "Ключевые слова для поиска:",

        "ai_prompt": "Придумай",
        "ai_prompt_unique_keywords": "уникальных и интересных ключевых словосочетаний для поиска в Telegram,",
        "ai_prompt_based_on": "на основе текста пользователя:",
        "ai_prompt_return_format": "Верни результат в формате простого списка, каждое слово на новой строке, без нумерации и дополнительных символов.",

    },
    "en": {
        "title": "TelegramMaster-Search-GPT",

        "menu_1": "1 - Data Processing",
        "menu_2": "2 - Settings",
        "menu_3": "3 - Documentation",
        "menu_4": "4 - Get parsed data",

        "select_action": "Select an action: ",
        "select_action_1": "Enter the model number:",
        "select_action_2": "Enter the api_id:",
        "select_action_3": "Enter api_hash:",
        "select_action_4": "Enter the number of variations of the names of the groups suggested by the artificial intelligence:",

        "settings_title": "Settings",

        "settings_1": "1 - Select AI model",
        "settings_2": "2 - Enter api_id and api_hash",
        "settings_4": "4 - Change language",
        "settings_5": "5 - Change the number of suggested AI groups",

        "ai_model_select": "Select AI Model",
        "ai_model_select_1": "Answer from AI:",
        "ai_model_select_2": "Choose an AI model:",
        "ai_model_select_3": "Error: incorrect selection.",
        "ai_model_select_4": "Введите сообщение для ИИ: ",

        "api_id_entry": "Enter api_id",
        "api_hash_entry": "Enter api_hash",
        "docs_open": "Open Documentation",
        "invalid_input": "Invalid input",
        "select_language": "Select language",
        "invalid_language_choice": "Invalid language choice, using saved language",
        "change_language": "Change language",
        "language_changed": "Language successfully changed",

        "error": "Account error:",
        "error_1": "Flood error:",

        "messages": "Search keywords:",

        "ai_prompt": "Come up with",
        "ai_prompt_unique_keywords": "unique and interesting keyword phrases for searching in Telegram,",
        "ai_prompt_based_on": "based on the user's text:",
        "ai_prompt_return_format": "Return the result as a simple list, each word on a new line, without numbering or extra symbols.",

    }
}

# Глобальная переменная для текущего языка
current_language = "ru"  # По умолчанию русский


def set_language(lang):
    global current_language
    if lang in translations:
        current_language = lang


def get_text(key):
    return translations[current_language].get(key, key)  # Если ключ не найден, возвращаем сам ключ
