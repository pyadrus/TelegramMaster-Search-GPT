# -*- coding: utf-8 -*-
import flet as ft

from core.buttons import create_buttons
from core.config import read_config_file
from core.file_utils import saving_changes_in_config_ini, save_language
from core.localization import get_text, set_language
from core.views import view_with_elements, program_title


async def record_setting(page: ft.Page):
    """
    Запись лимитов на аккаунт или сообщение

    :param page: Страница интерфейса Flet для отображения элементов управления.
    """
    lv = ft.ListView(expand=10, spacing=1, padding=2, auto_scroll=True)
    page.controls.append(lv)  # добавляем ListView на страницу для отображения логов 📝
    lv.controls.append(ft.Text(f"Введите данные для записи"))  # отображаем сообщение в ListView
    number_of_groups = ft.TextField(label=get_text("select_action_4"), multiline=True, max_lines=19)

    async def btn_click(e) -> None:
        await update_config_value(section='ai', option='number_of_groups', value=number_of_groups.value)
        page.go("/")  # Изменение маршрута в представлении существующих настроек
        page.update()

    await add_view_with_fields_and_button(page, [number_of_groups], btn_click, lv)


async def change_language(page: ft.Page):
    """Функция для смены языка в настройках программы"""
    page.views.clear()
    lv = ft.ListView(expand=10, spacing=1, padding=2, auto_scroll=True)
    page.controls.append(lv)
    lv.controls.append(ft.Text("Настройки программы\n\n"))
    page.update()

    async def _change_language_ru(_):
        """Смена языка на русский"""
        set_language("ru")
        save_language("ru")
        print(f"[green]{get_text('language_changed')}")

    async def _change_language_en(_):
        """Смена языка на английский"""
        set_language("en")
        save_language("en")
        print(f"[green]{get_text('language_changed')}")

    await view_with_elements(page=page, title=await program_title(title="⚙️ Смена языка"),
                             buttons=[
                                 await create_buttons(text=f"Русский", on_click=_change_language_ru),
                                 await create_buttons(text=f"English", on_click=_change_language_en),
                                 await create_buttons(text="⬅️ Назад", on_click=lambda _: page.go("/"))
                             ],
                             route_page="/",
                             lv=lv)
    page.update()  # Обновляем страницу


async def writing_api_id_api_hash(page: ft.Page):
    """
    Записываем api, hash полученный с помощью регистрации приложения на сайте https://my.telegram.org/auth
    """
    page.views.clear()
    page.update()

    lv = ft.ListView(expand=10, spacing=1, padding=2, auto_scroll=True)
    page.controls.append(lv)
    lv.controls.append(ft.Text("Настройки программы\n\n"))
    page.update()
    lv.controls.append(ft.Text("Ввод api_id и api_hash"))

    api_id_data = ft.TextField(label="Введите api_id", multiline=True, max_lines=19)
    api_hash_data = ft.TextField(label="Введите api_hash", multiline=True, max_lines=19)

    async def btn_click(e) -> None:
        await update_config_value(section='telegram_settings', option='api_id', value=api_id_data.value)
        await update_config_value(section='telegram_settings', option='api_hash', value=api_hash_data.value)
        page.go("/")
        page.update()

    await add_view_with_fields_and_button(
        page=page,
        fields=[api_id_data, api_hash_data],
        buttons=btn_click,
        lv=lv
    )


async def add_view_with_fields_and_button(page: ft.Page, fields: list, buttons, lv) -> None:
    """
    Добавляет представление с заданными текстовыми полями и кнопкой.
    """

    def back_button_clicked(e) -> None:
        page.go("/")

    # Исправлен порядок создания view и добавление его в page.views
    view = ft.View(
        "/",
        controls=[
            lv,
            ft.Column(
                controls=fields + [
                    await create_buttons(text="✅ Готово", on_click=buttons),
                    await create_buttons(text="⬅️ Назад", on_click=back_button_clicked),
                ]
            )
        ]
    )
    page.views.append(view)
    page.update()


async def select_and_save_model(page: ft.Page, section, option):
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

    dropdown = ft.Dropdown(
        label=get_text('ai_model_select_2'),
        options=[ft.dropdown.Option(key=key, text=value) for key, value in ai_list.items()],
        width=300,
    )

    message_container = ft.Container(content=ft.Text(""))

    async def on_save(e):
        selected_key = dropdown.value
        if selected_key in ai_list:
            selected_value = ai_list[selected_key]
            await update_config_value(section, option, selected_value)
            message_container.content = ft.Text(f"Выбрана модель: {selected_value}")
        else:
            message_container.content = ft.Text(f"{get_text('ai_model_select_3')}")
        page.update()

    save_button = ft.ElevatedButton(text="Сохранить", on_click=on_save)
    b_button = ft.ElevatedButton(text="⬅️ Назад", on_click=lambda _: page.go("/"))

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
    config = read_config_file()
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, value)
    await saving_changes_in_config_ini(config)
