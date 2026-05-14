import flet as ft

FORM_LOGIN_STYLE = {
    "width": 450,
    "height": 550,
    "padding": 36,
    "bgcolor": ft.Colors.WHITE,
    "border_radius": 20,
    "border": ft.border.all(1, ft.Colors.BLUE_100),
    "shadow": ft.BoxShadow(
        color=ft.Colors.with_opacity(0.10, ft.Colors.BLUE_900),
        blur_radius=30,
        offset=ft.Offset(0, 6),
    ),
}

FORM_REGISTER_STYLE = {
    "width": 450,
    "padding": 36,
    "bgcolor": ft.Colors.WHITE,
    "border_radius": 20,
    "border": ft.border.all(1, ft.Colors.BLUE_100),
    "shadow": ft.BoxShadow(
        color=ft.Colors.with_opacity(0.10, ft.Colors.BLUE_900),
        blur_radius=30,
        offset=ft.Offset(0, 6),
    ),
}