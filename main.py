# -*- coding: utf-8 -*-
import webbrowser

import flet as ft
from loguru import logger

from core.buttons import create_buttons
from core.config import program_name
from core.getting_data import getting_data_from_database
from core.localization import get_text
from core.logging_in import loging
from core.settings import select_and_save_model, writing_api_id_api_hash, change_language, record_setting
from core.telegram import search_and_save_telegram_groups
from core.views import TITLE_FONT_WEIGHT, PRIMARY_COLOR, view_with_elements, program_title

logger.add('user_data/log/log.log')


async def handle_settings(page: ft.Page):
    """Меню настроек"""
    page.views.clear()
    lv = ft.ListView(expand=10, spacing=1, padding=2, auto_scroll=True)
    page.controls.append(lv)
    lv.controls.append(ft.Text(get_text('text_settings_title')))
    page.update()

    async def select_ai_model(_):
        """Выбор модели AI"""
        await select_and_save_model(page=page, section='Settings', option='selectedmodel')

    async def enter_api_id_api_hash(_):
        """API_ID, API_HASH"""
        await writing_api_id_api_hash(page)

    async def _change_language(_):
        """Смена языка"""
        await change_language(page)

    async def change_the_number_of_suggested_ai_groups(_):
        """Изменение количества предложенных групп AI"""
        await record_setting(page)

    await view_with_elements(page=page, title=await program_title(title=get_text('settings_title')),
                             buttons=[
                                 await create_buttons(text=get_text('settings_1'), on_click=select_ai_model),
                                 await create_buttons(text=get_text('settings_2'), on_click=enter_api_id_api_hash),
                                 await create_buttons(text=get_text('settings_4'), on_click=_change_language),
                                 await create_buttons(text=get_text('settings_5'),
                                                      on_click=change_the_number_of_suggested_ai_groups),
                                 await create_buttons(text=get_text("button_back"), on_click=lambda _: page.go("/"))
                             ],
                             route_page="change_name_description_photo",
                             lv=lv)
    page.update()  # Обновляем страницу


class Application:
    """Класс для управления приложением."""

    def __init__(self):
        self.page = None
        self.info_list = None
        self.WINDOW_WIDTH = 900
        self.WINDOW_HEIGHT = 600
        self.SPACING = 5
        self.RADIUS = 5
        self.LINE_COLOR = ft.colors.GREY
        self.BUTTON_HEIGHT = 40
        self.LINE_WIDTH = 1
        self.PADDING = 10
        self.BUTTON_WIDTH = 300
        self.PROGRAM_MENU_WIDTH = self.BUTTON_WIDTH + self.PADDING

    async def actions_with_the_program_window(self, page: ft.Page):
        """Изменение на изменение главного окна программы."""
        page.title = get_text('text_title')
        page.window.width = self.WINDOW_WIDTH
        page.window.height = self.WINDOW_HEIGHT
        page.window.resizable = False
        page.window.min_width = self.WINDOW_WIDTH
        page.window.max_width = self.WINDOW_WIDTH
        page.window.min_height = self.WINDOW_HEIGHT
        page.window.max_height = self.WINDOW_HEIGHT

    def create_title(self, text: str, font_size) -> ft.Text:
        """Создает заголовок с градиентом."""
        return ft.Text(
            spans=[
                ft.TextSpan(
                    text,
                    ft.TextStyle(
                        size=font_size,
                        weight=TITLE_FONT_WEIGHT,
                        foreground=ft.Paint(
                            gradient=ft.PaintLinearGradient(
                                (0, 20), (150, 20), [PRIMARY_COLOR, PRIMARY_COLOR]
                            )), ), ), ], )

    def create_button(self, text: str, route: str) -> ft.OutlinedButton:
        """Создает кнопку меню."""
        return ft.OutlinedButton(
            text=text,
            on_click=lambda _: self.page.go(route),
            width=self.BUTTON_WIDTH,
            height=self.BUTTON_HEIGHT,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=self.RADIUS)),
        )

    def build_menu(self) -> ft.Column:
        """Создает колонку с заголовками и кнопками."""
        title = self.create_title(text=program_name, font_size=19)
        version = self.create_title(text=get_text('text_title_version'), font_size=13)
        date_program_change = self.create_title(text=get_text('text_title_date'), font_size=13)
        buttons = [
            self.create_button(get_text('menu_1'), "/data_processing"),
            self.create_button(get_text('menu_2'), "/settings"),
            self.create_button(get_text('menu_3'), "/documentation"),
            self.create_button(get_text('menu_4'), "/get_parsed_data"),
        ]
        return ft.Column(
            [title, version, date_program_change, *buttons],
            alignment=ft.MainAxisAlignment.START,
            spacing=self.SPACING,
        )

    async def setup(self):
        """Настраивает страницу."""
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.on_route_change = self.route_change
        await self.actions_with_the_program_window(self.page)
        self._add_startup_message()
        await self.route_change(None)

    def _add_startup_message(self):
        """Добавляет стартовое сообщение в ListView."""
        self.info_list.controls.append(ft.Text(get_text('text_main_page')))

    async def route_change(self, route):
        """Обработчик изменения маршрута."""
        self.page.views.clear()
        layout = ft.Row(
            [
                ft.Container(self.build_menu(), width=self.PROGRAM_MENU_WIDTH, padding=self.PADDING),
                ft.Container(width=self.LINE_WIDTH, bgcolor=self.LINE_COLOR),
                ft.Container(self.info_list, expand=True, padding=self.PADDING),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0,
            expand=True,
        )
        self.page.views.append(ft.View("/", [layout]))
        route_handlers = {
            "/data_processing": self._handle_data_processing,
            "/documentation": self._handle_documentation,
            "/settings": self._handle_settings,
            "/get_parsed_data": self._get_parsed_data,
        }
        handler = route_handlers.get(self.page.route)
        if handler:
            await handler()
        self.page.update()

    async def _handle_data_processing(self):
        """Перебор данных"""
        await search_and_save_telegram_groups(self.page)

    async def _handle_settings(self):
        """Страница ⚙️ Настройки программы"""
        await handle_settings(self.page)

    async def _handle_documentation(self):
        """Страница 📖 Документация"""
        webbrowser.open('https://github.com/pyadrus/TelegramMaster-Search-GPT/wiki', new=2)

    async def _get_parsed_data(self):
        """Страница Получение спарсенных данных"""
        await getting_data_from_database()

    async def main(self, page: ft.Page):
        """Точка входа в приложение."""
        self.page = page
        self.info_list = ft.ListView(expand=True, spacing=10, padding=self.PADDING, auto_scroll=True)

        await self.setup()
        await loging()


if __name__ == '__main__':
    # asyncio.run(main())

    ft.app(target=Application().main)
