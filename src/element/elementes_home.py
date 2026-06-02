
from src.styles.card_styles_home import *
from src.api.weather_api import get_forecast
from src.styles.dropdown_styles import CITY_DROPDOWN
from src.data.city import CITIES
from src.styles.button_styles import PRIMARY_BUTTON_STYLE


def element_home():
    weather_text = ft.Text("", size=15, weight=ft.FontWeight.BOLD)
    city_dd = ft.Dropdown(
        **CITY_DROPDOWN,
        options=[
            ft.DropdownOption(key=v, text=k)
            for k, v in CITIES.items()
        ],
    )

    def get_weather(e):
        try:
            data = get_forecast(city_dd.value)
            temp = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            weather_text.value = f"{temp}°C -  {condition}"
            weather_text.update()
        except Exception as ex:
            print(ex)

    return ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Популярні риби", **POPULAR_TITLE),
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Card(
                                        **FISH_CARD,
                                        content=ft.Container(
                                            content=ft.Image(src="карась.jpg", **FISH_IMAGE),
                                            **FISH_CONTAINER,
                                        ),
                                    ),
                                    ft.Text("Карась мирна риба, любить спокійні водойми.", **FISH_NAME_TEXT),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Card(
                                        **FISH_CARD,
                                        content=ft.Container(
                                            content=ft.Image(src="короп.jpg", **FISH_IMAGE),
                                            **FISH_CONTAINER,
                                        ),
                                    ),
                                    ft.Text("Короп велика та сильна прісноводна риба.", **FISH_NAME_TEXT),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                            ),
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Card(
                                        **FISH_CARD,
                                        content=ft.Container(
                                            content=ft.Image(src="судак.jpg", **FISH_IMAGE),
                                            **FISH_CONTAINER,
                                        ),
                                    ),
                                    ft.Text("Судак хижа риба з гострими зубами.", **FISH_NAME_TEXT),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Card(
                                        **FISH_CARD,
                                        content=ft.Container(
                                            content=ft.Image(src="щука.jpg", **FISH_IMAGE),
                                            **FISH_CONTAINER,
                                        ),
                                    ),
                                    ft.Text("Щука хижа риба, що полює із засідки.", **FISH_NAME_TEXT),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5,
                            ),
                        ],
                        spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.START,
                spacing=20,
                expand=True,
            ),

            ft.Column(
                controls=[

                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.SUNNY, size=28),
                            ft.Column(
                                controls=[
                                    ft.Text("Погода:", **WEATHER_LABEL),
                                    ft.Row(
                                        [
                                            city_dd,
                                            ft.Button(
                                                "Шукати погоду",
                                                style=PRIMARY_BUTTON_STYLE,
                                                on_click=get_weather,
                                            ),
                                        ]
                                    ),
                                    weather_text,
                                ],
                                spacing=6,
                            ),
                        ],
                        spacing=14,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),

                    ft.Divider(height=1),

                    ft.Row(
                        controls=[
                            ft.Text("Поради для рибака", **TIP_TITLE),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls=[
                            ft.Card(
                                **TIP_CARD,
                                content=ft.Container(
                                    content=ft.Stack(
                                        controls=[
                                            ft.Image(
                                                src="фон_цікаві_факти.jpg",
                                                **TIP_IMAGE,
                                            ),
                                            ft.Container(
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            "Найкраще клювання буває рано вранці "
                                                            "або перед заходом сонця. "
                                                            "У похмуру погоду риба часто "
                                                            "активніша біля берега.",
                                                            size=20,
                                                            color=ft.Colors.WHITE,
                                                            text_align=ft.TextAlign.CENTER,
                                                        ),
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                    spacing=10,
                                                ),
                                                alignment=ft.Alignment.CENTER,
                                                bgcolor=ft.Colors.BLACK54,
                                                width=TIP_IMAGE["width"],
                                                height=TIP_IMAGE["height"],
                                                border_radius=12,
                                                padding=20,
                                            ),
                                        ]
                                    ),
                                    **TIP_CONTAINER,
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                ],
                horizontal_alignment=ft.CrossAxisAlignment.START,
                alignment=ft.MainAxisAlignment.START,
                spacing=16,
                expand=True,
            ),

        ],
        vertical_alignment=ft.CrossAxisAlignment.START,
        expand=True,
    )
