import flet as ft

NOTE_CARD = {
    "elevation": 3,
    "shadow_color": ft.Colors.BLUE_200,
}

NOTE_CARD_CONTAINER = {
    "padding": ft.Padding.symmetric(horizontal=20, vertical=16),
    "border_radius": 12,
    "bgcolor": ft.Colors.WHITE,
    "shadow": ft.BoxShadow(
        spread_radius=1,
        blur_radius=10,
        color=ft.Colors.with_opacity(0.15, ft.Colors.BLUE_300),
        offset=ft.Offset(0, 4),
    ),
}

SORT_BUTTON = {
    "style": ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=8),
        padding=ft.Padding.symmetric(horizontal=20, vertical=12),
        text_style=ft.TextStyle(size=14, weight=ft.FontWeight.W_500),
        bgcolor=ft.Colors.BLUE_500,
        color=ft.Colors.WHITE,
    ),
}

SECTION_TITLE = {
    "size": 18,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_700,
}

NOTE_FISH_TEXT = {
    "size": 17,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_GREY_900,
}

NOTE_DATE_TEXT = {
    "size": 13,
    "weight": ft.FontWeight.W_500,
    "color": ft.Colors.BLUE_GREY_900,
}

NOTE_DETAIL_TEXT = {
    "size": 15,
    "weight": ft.FontWeight.W_500,
    "color": ft.Colors.BLUE_GREY_900,
}

NOTE_DESC_TEXT = {
    "size": 14,
    "weight": ft.FontWeight.W_500,
    "color": ft.Colors.BLUE_GREY_900,
    "italic": True,
}

EDIT_ICON = {
    "icon": ft.Icons.EDIT_OUTLINED,
    "icon_size": 20,
    "tooltip": "Редагувати",
    "icon_color": ft.Colors.BLUE_400,
    "padding": ft.Padding.all(4),
}

DELETE_ICON = {
    "icon": ft.Icons.DELETE_OUTLINE,
    "icon_size": 20,
    "tooltip": "Видалити",
    "icon_color": ft.Colors.RED_300,
    "padding": ft.Padding.all(4),
}

FORM_CONTAINER = {
    "padding": ft.Padding.all(20),
    "border_radius": 16,
    "bgcolor": ft.Colors.WHITE,
    "shadow": ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.Colors.with_opacity(0.15, ft.Colors.BLUE_300),
        offset=ft.Offset(0, 4),
    ),
}

SAVE_BUTTON_STYLE = ft.ButtonStyle(
    shape=ft.RoundedRectangleBorder(radius=10),
    padding=ft.Padding.symmetric(horizontal=24, vertical=14),
    text_style=ft.TextStyle(size=15, weight=ft.FontWeight.W_600),
    bgcolor=ft.Colors.BLUE_500,
    color=ft.Colors.WHITE,
)

DATE_TIME_TEXT = {
    "size": 14,
    "weight": ft.FontWeight.W_500,
    "color": ft.Colors.BLUE_700,
}
