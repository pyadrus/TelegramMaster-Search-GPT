# -*- coding: utf-8 -*-
from core.config import language, program_name, program_version, date_of_program_change

translations = {
    "ru": {
        "title": "TelegramMaster-Search-GPT",

        "menu_1": "📊 Перебор данных",
        "menu_2": "⚙️ Настройки",
        "menu_3": "📖 Документация",
        "menu_4": "📥 Получение спарсеных данных",

        "select_action": "🔍 Выберите действие: ",
        "select_action_1": "#️⃣ Введите номер модели: ",
        "select_action_2": "🔑 Введите api_id: ",
        "select_action_3": "🔐 Введите api_hash: ",
        "select_action_4": "🤖 Введите количество вариаций названий групп, предложенных ИИ: ",

        "settings_title": "⚙️ Настройки",

        "settings_1": "🤖 Выбор модели ИИ",
        "settings_2": "🔑 Запись api_id и api_hash",
        "settings_4": "🌐 Сменить язык",
        "settings_5": "🔢 Сменить количество предложенных групп ИИ",

        "ai_model_select": "🤖 Выбор модели ИИ",
        "ai_model_select_1": "💬 Ответ от ИИ:",
        "ai_model_select_2": "👇 Выберите модель ИИ:",
        "ai_model_select_3": "❌ Ошибка: некорректный выбор.",
        "ai_model_select_4": "✍️ Введите сообщение для ИИ: ",
        "ai_model_select_5": "✅ Выбрана модель: ",

        "api_id_entry": "🔑 Введите api_id",
        "api_hash_entry": "🔐 Введите api_hash",
        "docs_open": "📖 Открыть документацию",
        "invalid_input": "🚫 Некорректный ввод",
        "select_language": "🌐 Выберите язык",
        "invalid_language_choice": "⚠️ Некорректный выбор языка, используется сохранённый",
        "change_language": "🌐 Сменить язык",
        "language_changed": "✅ Язык успешно изменён",
        "language_changed_1": "⚙️ Смена языка",

        "error": "⚠️ Ошибка аккаунта: ",
        "error_1": "⏳ Ошибка флуда: ",

        "messages": "🔍 Ключевые слова для поиска:",

        "ai_prompt": "💡 Придумай",
        "ai_prompt_unique_keywords": "🔍 уникальных и интересных ключевых словосочетаний для поиска в Telegram,",
        "ai_prompt_based_on": "📝 на основе текста пользователя:",
        "ai_prompt_return_format": "📋 Верни результат в формате простого списка, каждое слово на новой строке, без нумерации и дополнительных символов.",

        "text_main_page": f"{program_name} 🚀\n\n{program_name} - программа для поиска групп/каналов по ключевым словам 💬\n\n"
                          f"📂 Проект доступен на GitHub: https://github.com/pyadrus/TelegramMaster-Search-GPT \n"
                          f"📲 Контакт с разработчиком в Telegram: https://t.me/PyAdminRU\n"
                          f"📡 Информация на канале: https://t.me/master_tg_d",
        "text_title": f"Версия {program_version}. Дата изменения {date_of_program_change}",
        "text_title_version": f"Версия программы: {program_version}",
        "text_title_date": f"Дата изменения: {date_of_program_change}",
        "text_data_processing": "✍️ Введите данные для записи",
        "button_done": "✅ Готово",
        "button_back": "⬅️ Назад",
        "button_save": "💾 Сохранить",
        "text_settings_title": "⚙️ Настройки программы\n\n",
    },
    "en": {
        "title": "TelegramMaster-Search-GPT",

        "menu_1": "📊 Data Processing",
        "menu_2": "⚙️ Settings",
        "menu_3": "📖 Documentation",
        "menu_4": "📥 Get parsed data",

        "select_action": "🔍 Select an action: ",
        "select_action_1": "#️⃣ Enter the model number:",
        "select_action_2": "🔑 Enter the api_id:",
        "select_action_3": "🔐 Enter api_hash:",
        "select_action_4": "🤖 Enter the number of variations of the names of the groups suggested by the artificial intelligence:",

        "settings_title": "⚙️ Settings",

        "settings_1": "🤖 Select AI model",
        "settings_2": "🔑 Enter api_id and api_hash",
        "settings_4": "🌐 Change language",
        "settings_5": "🔢 Change the number of suggested AI groups",

        "ai_model_select": "🤖 Select AI Model",
        "ai_model_select_1": "💬 Answer from AI:",
        "ai_model_select_2": "👇 Choose an AI model:",
        "ai_model_select_3": "❌ Error: incorrect selection.",
        "ai_model_select_4": "✍️ Enter a message for AI: ",
        "ai_model_select_5": "✅ Model selected: ",

        "api_id_entry": "🔑 Enter api_id",
        "api_hash_entry": "🔐 Enter api_hash",
        "docs_open": "📖 Open Documentation",
        "invalid_input": "🚫 Invalid input",
        "select_language": "🌐 Select language",
        "invalid_language_choice": "⚠️ Invalid language choice, using saved language",
        "change_language": "🌐 Change language",
        "language_changed": "✅ Language successfully changed",
        "language_changed_1": "⚙️ Language change",

        "error": "⚠️ Account error:",
        "error_1": "⏳ Flood error:",

        "messages": "🔍 Search keywords:",

        "ai_prompt": "💡 Come up with",
        "ai_prompt_unique_keywords": "🔍 unique and interesting keyword phrases for searching in Telegram,",
        "ai_prompt_based_on": "📝 based on the user's text:",
        "ai_prompt_return_format": "📋 Return the result as a simple list, each word on a new line, without numbering or extra symbols.",

        "text_main_page": f"{program_name} 🚀\n\n{program_name} is a program for searching groups/channels by keywords 💬\n\n"
                          f"📂 The project is available on GitHub: https://github.com/pyadrus/TelegramMaster-Search-GPT\n"
                          f"📲 Contact with the developer in Telegram: https://t.me/PyAdminRU\n"
                          f"📡 Information on the channel: https://t.me/master_tg_d",
        "text_title": f"Version {program_version}. Date of change {date_of_program_change}",
        "text_title_version": f"Program version: {program_version}",
        "text_title_date": f"Date of change: {date_of_program_change}",
        "text_data_processing": "✍️ Enter the data for recording",
        "button_done": "✅ Done",
        "button_back": "⬅️ Back",
        "button_save": "💾 Save",
        "text_settings_title": "⚙️ Program settings\n\n",
    }
}


def get_text(key):
    return translations[language].get(key, key)  # Если ключ не найден, возвращаем сам ключ
