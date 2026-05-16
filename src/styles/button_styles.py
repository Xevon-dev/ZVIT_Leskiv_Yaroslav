import flet as ft

# Головна кнопка (наприклад "Шукати погоду") — ширша, квадратніша
PRIMARY_BUTTON_STYLE = ft.ButtonStyle(
    color=ft.Colors.WHITE,
    bgcolor=ft.Colors.BLUE_500,
    overlay_color=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
    elevation=2,
    shape=ft.RoundedRectangleBorder(radius=10),
    padding=ft.Padding.symmetric(horizontal=40, vertical=16),
    text_style=ft.TextStyle(
        size=15,
        weight=ft.FontWeight.BOLD,
        letter_spacing=0.5,
    ),
)

# Навігаційні кнопки в AppBar — ширші, з тінню, виразніші
NAV_BUTTON_STYLE = ft.ButtonStyle(
    color=ft.Colors.BLUE_700,
    bgcolor=ft.Colors.WHITE,
    overlay_color=ft.Colors.with_opacity(0.08, ft.Colors.BLUE_400),
    elevation=0,
    shadow_color=ft.Colors.with_opacity(0.12, ft.Colors.BLUE_300),
    shape=ft.RoundedRectangleBorder(radius=10),
    padding=ft.Padding.symmetric(horizontal=22, vertical=11),
    side=ft.BorderSide(1.5, ft.Colors.BLUE_200),
    text_style=ft.TextStyle(
        size=14,
        weight=ft.FontWeight.W_700,
        letter_spacing=0.3,
    ),
)

TEXT_BUTTON_STYLE = ft.ButtonStyle(
    color=ft.Colors.BLUE_600,
    text_style=ft.TextStyle(
        size=14,
        weight=ft.FontWeight.W_500,
    ),
)