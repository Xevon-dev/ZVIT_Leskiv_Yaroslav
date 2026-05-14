import flet as ft
from src.styles.card_styles_notes import *


WEATHER_ICONS = {
    "sun":   ft.Icons.WB_SUNNY_OUTLINED,
    "cloud": ft.Icons.CLOUD_OUTLINED,
    "rain":  ft.Icons.UMBRELLA,
    "wind":  ft.Icons.AIR,
}

WEATHER_LABELS = {
    "sun":   "Сонячно",
    "cloud": "Хмарно",
    "rain":  "Дощ",
    "wind":  "Вітряно",
}


def build_note_card(note: dict, on_delete, on_edit):
    weather_key = note.get("weather", "")

    def handle_edit(e):
        on_edit(note)

    def handle_delete(e):
        on_delete(note)

    return ft.Card(
        **NOTE_CARD,
        content=ft.Container(
            **NOTE_CARD_CONTAINER,
            content=ft.Column(
                spacing=8,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(f"🐟 {note['fish']}  •  {note['weight']} кг", **NOTE_FISH_TEXT),
                            ft.Row(
                                spacing=0,
                                controls=[
                                    ft.IconButton(**EDIT_ICON,   on_click=handle_edit),
                                    ft.IconButton(**DELETE_ICON, on_click=handle_delete),
                                ],
                            ),
                        ],
                    ),

                    ft.Divider(height=1, color=ft.Colors.BLUE_GREY_100),


                    ft.Row(
                        spacing=8,
                        controls=[
                            ft.Icon(ft.Icons.LOCATION_ON_OUTLINED, size=16, color=ft.Colors.BLUE_GREY_400),
                            ft.Text(note["place"], **NOTE_DETAIL_TEXT),
                            ft.Container(width=12),
                            ft.Icon(WEATHER_ICONS.get(weather_key, ft.Icons.HELP_OUTLINE), size=16, color=ft.Colors.BLUE_GREY_400),
                            ft.Text(WEATHER_LABELS.get(weather_key, ""), **NOTE_DETAIL_TEXT),
                        ],
                    ),


                    ft.Row(
                        spacing=8,
                        controls=[
                            ft.Icon(ft.Icons.SET_MEAL_OUTLINED, size=16, color=ft.Colors.BLUE_GREY_400),
                            ft.Text(note["bait"], **NOTE_DETAIL_TEXT),
                        ],
                    ),


                    ft.Text(note["desc"], **NOTE_DESC_TEXT, visible=bool(note.get("desc"))),


                    ft.Row(
                        spacing=6,
                        controls=[
                            ft.Icon(ft.Icons.CALENDAR_TODAY_OUTLINED, size=13, color=ft.Colors.GREY_400),
                            ft.Text(note["date"], **NOTE_DATE_TEXT),
                            ft.Icon(ft.Icons.ACCESS_TIME, size=13, color=ft.Colors.GREY_400),
                            ft.Text(note["time"], **NOTE_DATE_TEXT),
                        ],
                    ),
                ],
            ),
        ),
    )