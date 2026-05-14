from src.styles.text_styles import WEATHER_TEXT
from src.styles.weather_card_styles import *
from src.api.weather_api import get_forecast
from src.data.city import CITIES
from src.element.recommendation_box import get_recommendation
from src.styles.dropdown_styles import CITY_DROPDOWN

DAYS_UA = ["Сьогодні", "Завтра", "Післязавтра"]


def build_weather_card(day_data: dict, day_label: str, rec_box: ft.Container):
    day = day_data["day"]
    temp = round(day["avgtemp_c"])
    condition = day["condition"]["text"]
    icon_url = "https:" + day["condition"]["icon"]
    wind = round(day["maxwind_kph"])
    humidity = round(day["avghumidity"])
    precip = day["totalprecip_mm"]
    pressure = round(day_data["hour"][12]["pressure_mb"] * 0.750062)

    def row(label, value):
        return ft.Row(
            controls=[
                ft.Text(label, **PARAM_LABEL, expand=True),
                ft.Text(value, **PARAM_VALUE),
            ],
        )

    def on_recommend(e):
        rec_text = get_recommendation(wind, precip, pressure)
        rec_box.content = ft.Column(
            controls=[
                ft.Text(f"Рекомендації - {day_label}", size=15, weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_GREY_900),
                ft.Divider(color=ft.Colors.BLUE_100),
                ft.Text(rec_text, size=14, weight=ft.FontWeight.W_600, color=ft.Colors.BLUE_GREY_800),
            ],
            spacing=13,
        )
        rec_box.visible = True
        rec_box.update()

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(day_label, **CITY_TEXT),
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(condition, **CONDITION_TEXT),
                                ft.Text(f"{temp}°C", **TEMP_TEXT),
                            ],
                            spacing=4,
                        ),
                        ft.Image(src=icon_url, width=64, height=64),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(color=ft.Colors.BLUE_50),
                row("💨 Вітер", f"{wind} км/год"),
                row("🌧 Опади", f"{precip} мм"),
                row("💧 Вологість", f"{humidity}%"),
                row("🔵 Тиск", f"{pressure} мм рт.ст."),
                ft.Container(height=8),
                ft.Button(
                    "Дізнатися рекомендації",
                    style=RECOMMEND_BTN,
                    on_click=on_recommend,
                ),
            ],
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
        **WEATHER_CARD,
    )


def weather_element():
    selected_city = {"value": None, "name": ""}
    cards_row = ft.Row(controls=[], spacing=16, wrap=False)

    local_rec_box = ft.Container(
        visible=False,
        width=420,
        padding=ft.padding.all(20),
        border_radius=16,
        bgcolor=ft.Colors.WHITE,
        border=ft.border.all(1, ft.Colors.BLUE_100),
        shadow=ft.BoxShadow(
            blur_radius=12,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLUE_900),
            offset=ft.Offset(0, 4),
        ),
    )

    def on_city_select(e):
        selected_city["value"] = e.control.value
        for k, v in CITIES.items():
            if v == e.control.value:
                selected_city["name"] = k
                break
        local_rec_box.visible = False
        local_rec_box.update()

    def on_search(e):
        city = selected_city["value"]
        if not city:
            return
        try:
            local_rec_box.visible = False
            local_rec_box.update()
            data = get_forecast(city)
            forecast_days = data["forecast"]["forecastday"]
            cards_row.controls = [
                build_weather_card(forecast_days[i], DAYS_UA[i], local_rec_box)
                for i in range(len(forecast_days))
            ]
            cards_row.update()
        except Exception as a:
            print(f"Помилка: {a}")

    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text("Щоб дізнатися погоду оберіть місто", weight= ft.FontWeight.BOLD , size= 20),
                    ft.Dropdown(
                        **CITY_DROPDOWN,
                        options=[
                            ft.DropdownOption(key=v, text=k)
                            for k, v in CITIES.items()
                        ],
                        on_select=on_city_select,
                    ),
                    ft.Button(
                        "Шукати погоду",
                        on_click=on_search,
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            bgcolor=ft.Colors.DEEP_PURPLE_400,
                            shape=ft.RoundedRectangleBorder(radius=24),
                        ),
                    ),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[cards_row, local_rec_box],
                spacing=20,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        spacing=20,
    )