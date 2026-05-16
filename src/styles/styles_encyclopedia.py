import flet as ft

IMAGE_CARD_CONTAINER = {
    "width": 380,
    "height": 200,
    "bgcolor": ft.Colors.BLUE_GREY_100,
    "border_radius": 12,
    "alignment": ft.Alignment(0, 0),
    "shadow": ft.BoxShadow(
        spread_radius=1,
        blur_radius=12,
        color=ft.Colors.with_opacity(0.18, ft.Colors.BLUE_GREY_900),
        offset=ft.Offset(0, 4),
    ),
}

IMAGE_CARD_ICON = {
    "color": ft.Colors.BLUE_GREY_300,
    "size": 90,
}

DESC_CARD_CONTAINER = {
    "height": 200,
    "padding": ft.Padding.symmetric(horizontal=20, vertical=16),
    "border_radius": 12,
    "shadow": ft.BoxShadow(
        spread_radius=1,
        blur_radius=12,
        color=ft.Colors.with_opacity(0.18, ft.Colors.BLUE_GREY_900),
        offset=ft.Offset(0, 4),
    ),
}

FISH_NAME_TEXT = {
    "size": 16,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_GREY_900,
}

FISH_DESC_TEXT = {
    "size": 16,
    "weight": ft.FontWeight.W_500,
    "color": ft.Colors.BLUE_GREY_900,
    "max_lines": 5,
    "overflow": ft.TextOverflow.ELLIPSIS,
}

ROW_CONTAINER = {
    "margin": ft.Margin.symmetric(horizontal=16, vertical=8),
}

SECTION_TITLE = {
    "size": 18,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_GREY_900,
}