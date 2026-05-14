import flet as ft
from src.models.audit_register_login import valid_email, audit_parol_letters, audit_parol_numbers
from src.data.user_json import read_json, save_json
from datetime import datetime

from src.styles.styles_container import FORM_REGISTER_STYLE
from src.styles.text_styles import TITLE_TEXT, SUBTITLE_TEXT
from src.styles.field_styles import INPUT_FIELD_STYLE
from src.styles.button_styles import PRIMARY_BUTTON_STYLE
from src.styles.checkbox_styles import CHECKBOX_STYLE


class RegisterView(ft.View):
    def __init__(self):
        self.user_login = ft.TextField(
            label="Логін",
            width=300,
            prefix_icon=ft.Icons.LOGIN,
            **INPUT_FIELD_STYLE
        )

        self.user_email = ft.TextField(
            label="Email",
            width=300,
            prefix_icon=ft.Icons.EMAIL,
            **INPUT_FIELD_STYLE
        )

        self.user_parol = ft.TextField(
            label="Пароль",
            width=300,
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.Icons.LOCK,
            **INPUT_FIELD_STYLE
        )

        self.user_parol_confirm = ft.TextField(
            label="Підтвердіть пароль",
            width=300,
            password=True,
            can_reveal_password=True,
            prefix_icon=ft.Icons.LOCK_OUTLINE,
            **INPUT_FIELD_STYLE
        )

        self.user_policy_checkbox = ft.Checkbox(
            label=ft.Text(
                "Погоджуюся з політикою конфеденційності",
                size=12
            ),
            **CHECKBOX_STYLE
        )

        self.user_button_register = ft.Button(
            "Зареєструватися",
            style=PRIMARY_BUTTON_STYLE,
            on_click=self.go_to_login
        )

        super().__init__(
            route="/register",
            controls=[
                ft.AppBar(
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        on_click=self.go_back
                    ),
                    title="Реєстрація",
                ),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,

                    content=ft.Container(
                        **FORM_REGISTER_STYLE,
                        content=ft.Column(
                            controls=[
                                ft.Text("Реєстрація", style=TITLE_TEXT),

                                ft.Text(
                                    "Створіть акаунт щоб продовжити",
                                    style=SUBTITLE_TEXT
                                ),

                                ft.Column(
                                    controls=[
                                        self.user_login,
                                        self.user_email,
                                        self.user_parol,
                                        self.user_parol_confirm,  # НОВЕ ПОЛЕ
                                        self.user_policy_checkbox,
                                        self.user_button_register,
                                    ],
                                    spacing=20,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                            ],
                            spacing=30,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                )
            ]
        )

    async def go_to_login(self, e):
        audit_user_login = self.user_login.value
        audit_user_email = self.user_email.value
        audit_user_parol = self.user_parol.value
        audit_user_parol_confirm = self.user_parol_confirm.value

        has_error = False

        if len(audit_user_login) < 5:
            self.user_login.error = "Мінімум 5 символів"
            has_error = True
        else:
            self.user_login.error = None

        if not valid_email(audit_user_email):
            self.user_email.error = "Введіть коректний email"
            has_error = True
        else:
            self.user_email.error = None

        if len(audit_user_parol) < 5:
            self.user_parol.error = "Мінімум 5 символів"
            has_error = True
        elif not audit_parol_letters(audit_user_parol):
            self.user_parol.error = "Додайте літери"
            has_error = True
        elif not audit_parol_numbers(audit_user_parol):
            self.user_parol.error = "Додайте цифри"
            has_error = True
        else:
            self.user_parol.error = None

        if audit_user_parol != audit_user_parol_confirm:
            self.user_parol_confirm.error = "Паролі не співпадають"
            has_error = True
        else:
            self.user_parol_confirm.error = None

        if not self.user_policy_checkbox.value:
            self.user_policy_checkbox.label = ft.Text(
                "Потрібно погодитись з політикою",
                size=12,
                color=ft.Colors.RED
            )
            has_error = True

        if has_error:
            return

        dani = read_json()

        new_user = {
            "login": audit_user_login,
            "email": audit_user_email,
            "parol": audit_user_parol,
            "created_at": datetime.now().strftime("%d.%m.%Y"),
            "notes": []
        }

        dani["users"].append(new_user)
        save_json(dani)

        await self.page.push_route("/login")

    async def go_back(self, e):
        await self.page.push_route("/login")
