# -*- coding: utf-8 -*-
import flet as ft

from core.config import read_config_file
from core.file_utils import saving_changes_in_config_ini
from core.localization import get_text


async def select_and_save_model(page: ft.Page, section, option):
    # Создаем список моделей
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

    # Создаем выпадающий список с опциями
    dropdown = ft.Dropdown(
        label=get_text('ai_model_select_2'),
        options=[ft.dropdown.Option(key=key, text=value) for key, value in ai_list.items()],
        width=300,
    )

    # Контейнер для сообщений
    message_container = ft.Container(content=ft.Text(""))

    # Функция обработки выбора
    async def on_save(e):
        selected_key = dropdown.value
        if selected_key in ai_list:
            selected_value = ai_list[selected_key]
            await update_config_value(section, option, selected_value)
            message_container.content = ft.Text(f"Выбрана модель: {selected_value}")
        else:
            message_container.content = ft.Text(f"{get_text('ai_model_select_3')}")
        page.update()

    # Кнопка для сохранения выбора
    save_button = ft.ElevatedButton(text="Сохранить", on_click=on_save)
    b_button = ft.ElevatedButton(text="⬅️ Назад", on_click=lambda _: page.go("/"))

    # Очищаем страницу и добавляем новый вид
    page.views.clear()
    page.views.append(
        ft.View(
            "/",
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(f"{get_text('ai_model_select')}\n", size=20, weight=ft.FontWeight.BOLD),
                        dropdown,
                        save_button,
                        b_button,
                        message_container
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True,
                    spacing=20
                )
            ],
            padding=20,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()


async def update_config_value(section, option, value):
    """Обновление значения в конфигурационном файле"""
    config = await read_config_file()
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, value)
    await saving_changes_in_config_ini(config)