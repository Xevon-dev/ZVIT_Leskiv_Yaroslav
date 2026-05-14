import flet as ft

CITY_DROPDOWN = {
    "width": 260,
    "hint_text": "Оберіть місто",
    "label": "Місто",
    "editable": True,
    "enable_filter": True,
    "leading_icon": ft.Icons.SEARCH,

    "border_radius": 14,
    "filled": True,
    "bgcolor": ft.Colors.WHITE,
    "border_color": ft.Colors.DEEP_PURPLE_200,
    "focused_border_color": ft.Colors.DEEP_PURPLE_500,

    "text_size": 15,
    "label_style": ft.TextStyle(
        size=14,
        color=ft.Colors.BLUE_GREY_700,
        weight=ft.FontWeight.W_500,
    ),

    "text_style": ft.TextStyle(
        size=15,
        color=ft.Colors.BLUE_GREY_900,
        weight=ft.FontWeight.W_500,
    ),
}