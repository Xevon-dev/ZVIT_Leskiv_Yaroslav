import flet as ft
from src.styles.styles_container import FORM_LOGIN_STYLE
from src.styles.text_styles import TITLE_TEXT, SUBTITLE_TEXT
from src.styles.field_styles import INPUT_FIELD_STYLE
from src.styles.button_styles import PRIMARY_BUTTON_STYLE, TEXT_BUTTON_STYLE
from src.data.user_json import *


class LoginView(ft.View):
    def __init__(self):
        self.user_login = ft.TextField(
            label="Логін",
            width=300,
            prefix_icon=ft.Icons.LOGIN,
            **INPUT_FIELD_STYLE
        )

        self.user_password = ft.TextField(
            label="Пароль",
            width=300,
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.Icons.LOCK,
            **INPUT_FIELD_STYLE
        )

        self.login_button = ft.Button(
            "Увійти",
            style=PRIMARY_BUTTON_STYLE,
            on_click=self.go_to_home
        )

        self.register_text = ft.TextButton(
            "Зареєструватися",
            style=TEXT_BUTTON_STYLE,
            on_click=self.go_to_register
        )

        super().__init__(
            route="/login",
            padding=0,
            controls=[
                ft.AppBar(
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        on_click=self.go_back
                    ),
                    title="Логінація",
                ),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,

                    content=ft.Container(
                        **FORM_LOGIN_STYLE,

                        content=ft.Column(
                            controls=[
                                ft.Text("Логін", style=TITLE_TEXT),

                                ft.Text(
                                    "Увійдіть у свій акаунт",
                                    style=SUBTITLE_TEXT
                                ),

                                ft.Column(
                                    controls=[
                                        self.user_login,
                                        self.user_password,
                                        self.login_button,
                                    ],
                                    spacing=20,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),

                                self.register_text,
                            ],
                            spacing=40,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                )
            ]
        )

    async def go_to_register(self):
        await self.page.push_route("/register")

    async def go_to_home(self, e):
        login = self.user_login.value
        password = self.user_password.value

        dani = read_json()
        user_found = None

        for user in dani["users"]:
            if user["login"] == login and user["parol"] == password:
                user_found = user
                break

        if not user_found:
            self.user_login.error = "Невірний логін або пароль"
            self.user_password.error = "Невірний логін або пароль"
            return

        dani["user_authorized"] = True
        dani["current_user"] = login
        save_json(dani)

        await self.page.push_route("/home")

    async def go_back(self, e):
        await self.page.push_route("/home")
