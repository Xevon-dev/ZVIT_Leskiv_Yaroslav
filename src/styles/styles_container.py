import flet as ft

FORM_LOGIN_STYLE = {
    "width": 450,
    "height": 550,
    "padding": 19,
    "bgcolor": ft.Colors.WHITE,
    "border_radius": 20,
    "shadow": ft.BoxShadow(
        color=ft.Colors.BLUE_GREY_900,
        blur_radius=25,
    ),
}

FORM_REGISTER_STYLE = {
    "width": 450,
    # "height": 550,  ← прибери або збільш до 650
    "padding": 19,
    "bgcolor": ft.Colors.WHITE,
    "border_radius": 20,
    "shadow": ft.BoxShadow(
        color=ft.Colors.BLUE_GREY_900,
        blur_radius=25,
    ),
}