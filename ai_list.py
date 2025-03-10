import configparser


def select_and_save_model():
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

    config = configparser.ConfigParser()
    config.read('config.ini', encoding='utf-8')

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
        with open('config.ini', 'w', encoding='utf-8') as configfile:
            config.write(configfile)

        print(f"Модель {selected_model} успешно сохранена в config.ini")
    else:
        print("Ошибка: некорректный выбор.")
