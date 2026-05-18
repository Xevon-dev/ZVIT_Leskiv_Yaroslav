import flet as ft
from datetime import datetime

from src.styles.text_styles import *
from src.element.weather_elementes import weather_element
from src.element.bottom_appbar import bottom_app_bar


class FishingWeatherViews(ft.View):

    def __init__(self):
        date = datetime.now().strftime("%d.%m.%Y")

        super().__init__(
            route="/fishing_weather",
            padding=0,
            controls=[
                ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Прогноз кльову"),
                            leading=ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                on_click=self.go_back
                            ),
                            actions=[
                                ft.Container(
                                    content=ft.Text(
                                        f"СЬОГОДНІ - {date}",
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    padding=ft.Padding.only(right=15),
                                    alignment=ft.Alignment.CENTER,
                                )
                            ],
                        ),

                        ft.Column(
                            controls=[
                                ft.Divider(),
                                weather_element(),
                            ],
                            expand=True,
                        ),

                        bottom_app_bar()
                    ]
                )
            ]
        )

    async def go_back(self, e):
        await self.page.push_route("/home")
