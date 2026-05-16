import flet as ft


NOTE_CARD = {
    "elevation": 3,
    "shadow_color": ft.Colors.BLUE_GREY_200,
}

NOTE_CARD_CONTAINER = {
    "padding": ft.Padding.symmetric(horizontal=20, vertical=16),
    "border_radius": 12,
}

SORT_BUTTON = {
    "style": ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=6),
        padding=ft.Padding.symmetric(horizontal=20, vertical=12),
        text_style=ft.TextStyle(size=14),
    ),
}

SECTION_TITLE = {
    "size": 16,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_GREY_900,
}

NOTE_FISH_TEXT = {
    "size": 17,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_GREY_900,
}


NOTE_DATE_TEXT = {
    "size": 13,
    "color": ft.Colors.GREY_500,
}


NOTE_DETAIL_TEXT = {
    "size": 15,
    "color": ft.Colors.BLUE_GREY_600,
}


NOTE_DESC_TEXT = {
    "size": 14,
    "color": ft.Colors.GREY_500,
    "italic": True,
}


EDIT_ICON = {
    "icon": ft.Icons.EDIT_OUTLINED,
    "icon_size": 20,
    "tooltip": "Редагувати",
    "icon_color": ft.Colors.BLUE_GREY_300,
    "padding": ft.Padding.all(4),
}


DELETE_ICON = {
    "icon": ft.Icons.DELETE_OUTLINE,
    "icon_size": 20,
    "tooltip": "Видалити",
    "icon_color": ft.Colors.RED_300,
    "padding": ft.Padding.all(4),
}