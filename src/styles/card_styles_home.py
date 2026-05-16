import flet as ft

POPULAR_TITLE = {
    "size": 22,
    "weight": ft.FontWeight.BOLD,
    "text_align": ft.TextAlign.CENTER,
    "color": ft.Colors.BLUE_GREY_900,
}

FISH_IMAGE = {
    "width": 340,
    "height": 210,
    "fit": "cover",
}

FISH_CARD = {
    "elevation": 0,
    "clip_behavior": ft.ClipBehavior.ANTI_ALIAS,
    "width": 340,
    "height": 210,
}

FISH_CONTAINER = {
    "border_radius": 14,
    "bgcolor": ft.Colors.WHITE,
    "border": ft.Border.all(1, ft.Colors.BLUE_100),
    "shadow": ft.BoxShadow(
        blur_radius=14,
        color=ft.Colors.with_opacity(0.10, ft.Colors.BLUE_600),
        offset=ft.Offset(0, 4),
    ),
    "expand": True,
}

FISH_NAME_TEXT = {
    "size": 13,
    "weight": ft.FontWeight.W_600,
    "text_align": ft.TextAlign.CENTER,
    "color": ft.Colors.BLUE_GREY_700,
}

TIP_TITLE = {
    "size": 22,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_GREY_900,
}

TIP_IMAGE = {
    "width": 600,
    "height": 320,
    "fit": "cover",
}

TIP_CARD = {
    "elevation": 0,
    "clip_behavior": ft.ClipBehavior.ANTI_ALIAS,
    "width": 600,
    "height": 320,
}

TIP_CONTAINER = {
    "border_radius": 14,
    "bgcolor": ft.Colors.WHITE,
    "border": ft.Border.all(1, ft.Colors.BLUE_100),
    "shadow": ft.BoxShadow(
        blur_radius=16,
        color=ft.Colors.with_opacity(0.10, ft.Colors.BLUE_900),
        offset=ft.Offset(0, 5),
    ),
    "expand": True,
}

WEATHER_LABEL = {
    "size": 13,
    "color": ft.Colors.BLUE_GREY_400,
}

WEATHER_VALUE = {
    "size": 17,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_700,
}