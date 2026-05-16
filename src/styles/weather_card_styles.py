import flet as ft


WEATHER_CARD = {
    "width": 280,
    "padding": ft.Padding.all(20),
    "border_radius": 16,
    "bgcolor": ft.Colors.WHITE,
    "border": ft.Border.all(1, ft.Colors.BLUE_100),
    "shadow": ft.BoxShadow(
        blur_radius=12,
        color=ft.Colors.with_opacity(0.1, ft.Colors.BLUE_900),
        offset=ft.Offset(0, 4),
    ),
}

CITY_TEXT = {
    "size": 18,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_GREY_900,
}


CONDITION_TEXT = {
    "size": 13,
    "color": ft.Colors.GREY_600,
}

TEMP_TEXT = {
    "size": 42,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_700,
}


PARAM_LABEL = {
    "size": 12,
    "color": ft.Colors.GREY_600,
}

PARAM_VALUE = {
    "size": 13,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_GREY_800,
}

RECOMMEND_BTN = ft.ButtonStyle(
    color=ft.Colors.WHITE,
    bgcolor=ft.Colors.DEEP_PURPLE_400,
    shape=ft.RoundedRectangleBorder(radius=20),
    padding=ft.Padding.symmetric(horizontal=20, vertical=10),
)
