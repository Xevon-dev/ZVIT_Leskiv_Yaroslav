import flet as ft


def bottom_app_bar():
    return ft.BottomAppBar(
        bgcolor=ft.Colors.BLUE_GREY_900,
        height=52,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[

                ft.Row(
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(ft.Icons.PHISHING, size=16, color=ft.Colors.LIGHT_BLUE_300),
                        ft.Text(
                            "© 2026 Рибальський застосунок",
                            color=ft.Colors.BLUE_GREY_300,
                            size=12,
                            weight=ft.FontWeight.W_500,
                        ),
                    ],
                ),

                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.FACEBOOK,
                            icon_color=ft.Colors.LIGHT_BLUE_300,
                            icon_size=18,
                            url="https://facebook.com",
                        ),
                        ft.IconButton(
                            icon=ft.Icons.TELEGRAM,
                            icon_color=ft.Colors.LIGHT_BLUE_300,
                            icon_size=18,
                            url="https://t.me",
                        ),
                        ft.IconButton(
                            icon=ft.Icons.PLAY_CIRCLE,
                            icon_color=ft.Colors.LIGHT_BLUE_300,
                            icon_size=18,
                            url="https://instagram.com",
                        ),
                    ],
                ),

                ft.Row(
                    spacing=0,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.TextButton(
                            "Зв'язатися з нами",
                            icon=ft.Icons.EMAIL_OUTLINED,
                            url="https://t.me/mynt_horia",
                            style=ft.ButtonStyle(
                                color={
                                    ft.ControlState.DEFAULT: ft.Colors.BLUE_GREY_300,
                                    ft.ControlState.HOVERED: ft.Colors.WHITE
                                },
                                icon_color={
                                    ft.ControlState.DEFAULT: ft.Colors.LIGHT_BLUE_300,
                                    ft.ControlState.HOVERED: ft.Colors.LIGHT_BLUE_300
                                },
                                text_style=ft.TextStyle(size=12),
                            ),
                        ),

                        ft.Container(
                            width=1,
                            height=16,
                            bgcolor=ft.Colors.with_opacity(0.13, ft.Colors.WHITE)
                        ),

                        ft.TextButton(
                            "Про нас",
                            icon=ft.Icons.INFO_OUTLINED,
                            url="https://uk.wikipedia.org/wiki/Рибальство",
                            style=ft.ButtonStyle(
                                color={
                                    ft.ControlState.DEFAULT: ft.Colors.BLUE_GREY_300,
                                    ft.ControlState.HOVERED: ft.Colors.WHITE
                                },
                                icon_color={
                                    ft.ControlState.DEFAULT: ft.Colors.LIGHT_BLUE_300,
                                    ft.ControlState.HOVERED: ft.Colors.LIGHT_BLUE_300
                                },
                                text_style=ft.TextStyle(size=12),
                            ),
                        ),

                        ft.Container(
                            width=1,
                            height=16,
                            bgcolor=ft.Colors.with_opacity(0.13, ft.Colors.WHITE)
                        ),

                        ft.TextButton(
                            "Політика конфіденційності",
                            icon=ft.Icons.PRIVACY_TIP_OUTLINED,
                            url="https://www.privacypolicies.com/",
                            style=ft.ButtonStyle(
                                color={
                                    ft.ControlState.DEFAULT: ft.Colors.BLUE_GREY_300,
                                    ft.ControlState.HOVERED: ft.Colors.WHITE
                                },
                                icon_color={
                                    ft.ControlState.DEFAULT: ft.Colors.LIGHT_BLUE_300,
                                    ft.ControlState.HOVERED: ft.Colors.LIGHT_BLUE_300
                                },
                                text_style=ft.TextStyle(size=12),
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )