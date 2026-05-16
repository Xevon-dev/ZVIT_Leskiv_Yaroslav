from datetime import datetime
import flet as ft
from src.styles.profile_style import *
from src.styles.field_styles import INPUT_FIELD_STYLE
from src.data.user_json import read_json, save_json
from src.models.audit_register_login import valid_email, audit_parol_letters, audit_parol_numbers


def profile_elements(page: ft.Page):
    dani = read_json()
    current_login = dani["current_user"]
    current_user = None
    for i in dani["users"]:
        if i["login"] == current_login:
            current_user = i
            break

    notes_count = len(current_user.get("notes", []))
    initials = current_login[:2].upper()

    created_at = current_user.get("created_at", "")
    days = 0
    if created_at:
        delta = datetime.now() - datetime.strptime(created_at, "%d.%m.%Y")
        days = delta.days

    avatar = ft.Container(
        **AVATAR_CONTAINER,
        content=ft.Text(initials, **AVATAR_TEXT),
    )

    stat_box = ft.Container(
        **STAT_BOX,
        content=ft.Row(
            **STAT_ROW,
            controls=[
                ft.Icon(ft.Icons.PHISHING, **STAT_ICON),
                ft.Text(f"{notes_count} нотаток", **STAT_TEXT),
            ],
        ),
    )

    tf_email = ft.TextField(
        label="Email",
        value=current_user["email"],
        width=280,
        prefix_icon=ft.Icons.EMAIL,
        visible=False,
        **INPUT_FIELD_STYLE,
    )
    tf_password = ft.TextField(
        label="Новий пароль",
        width=280,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        visible=False,
        **INPUT_FIELD_STYLE,
    )
    tf_password_confirm = ft.TextField(
        label="Підтвердіть пароль",
        width=280,
        password=True,
        can_reveal_password=True,
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        visible=False,
        **INPUT_FIELD_STYLE,
    )

    display_email = ft.Text(current_user["email"], **EMAIL_TEXT)

    edit_btn = ft.Button("Редагувати", icon=ft.Icons.EDIT_OUTLINED, on_click=None)
    save_btn = ft.Button("Зберегти", icon=ft.Icons.SAVE, style=SAVE_BUTTON_STYLE, visible=False, on_click=None)
    cancel_btn = ft.TextButton("Скасувати", visible=False, on_click=None)

    def toggle_edit(e=None):
        is_edit = not tf_email.visible
        tf_email.visible = is_edit
        tf_password.visible = is_edit
        tf_password_confirm.visible = is_edit
        save_btn.visible = is_edit
        cancel_btn.visible = is_edit
        edit_btn.visible = not is_edit
        if is_edit:
            tf_email.value = current_user["email"]
            tf_password.value = ""
            tf_password_confirm.value = ""
            tf_email.error = None
            tf_password.error = None
            tf_password_confirm.error = None

    def save_changes(e):
        new_email = tf_email.value.strip()
        new_pass = tf_password.value

        if not valid_email(new_email):
            tf_email.error = "Введіть коректний email"
            return
        else:
            tf_email.error = None

        if new_pass:
            if len(new_pass) < 5:
                tf_password.error = "Мінімум 5 символів"
                return
            elif not audit_parol_letters(new_pass):
                tf_password.error = "Додайте літери"
                return
            elif not audit_parol_numbers(new_pass):
                tf_password.error = "Додайте цифри"
                return
            else:
                tf_password.error = None
            if new_pass != tf_password_confirm.value:
                tf_password_confirm.error = "Паролі не співпадають"
                return
            else:
                tf_password_confirm.error = None

        current_user["email"] = new_email
        if new_pass:
            current_user["parol"] = new_pass

        data = read_json()
        for i in data["users"]:
            if i["login"] == current_login:
                i["email"] = new_email
                if new_pass:
                    i["parol"] = new_pass
                break
        save_json(data)

        display_email.value = new_email
        toggle_edit()

        dialog = ft.AlertDialog(
            title=ft.Text("Готово"),
            content=ft.Text("Дані успішно оновлено!"),
            open=True,
        )

        def close_dialog(e):
            page.pop_dialog()

        dialog.actions = [ft.TextButton("OK", on_click=close_dialog)]
        page.show_dialog(dialog)

    async def do_logout(e):
        data = read_json()
        data["user_authorized"] = False
        data["current_user"] = ""
        save_json(data)
        await page.push_route("/home")

    edit_btn.on_click = toggle_edit
    cancel_btn.on_click = toggle_edit
    save_btn.on_click = save_changes

    left_panel = ft.Container(
        **LEFT_PANEL,
        content=ft.Column(
            **LEFT_COLUMN,
            controls=[
                avatar,
                ft.Container(height=12),
                ft.Text(current_login, **LOGIN_TEXT),
                display_email,
                ft.Text(
                    f"Акаунту {days} днів" if created_at else "",
                    size=12,
                    color=ft.Colors.BLUE_GREY_400,
                    italic=True,
                ),
                ft.Container(height=10),
                stat_box,
                ft.Container(height=16),
                ft.TextButton(
                    "Вийти",
                    icon=ft.Icons.LOGOUT,
                    style=LOGOUT_BUTTON_STYLE,
                    on_click=do_logout,
                ),
            ],
        ),
    )

    right_panel = ft.Container(
        **RIGHT_PANEL,
        content=ft.Column(
            **RIGHT_COLUMN,
            controls=[
                ft.Text("Редагування профілю", **EDIT_TITLE_TEXT),
                ft.Divider(**EDIT_DIVIDER),
                edit_btn,
                tf_email,
                tf_password,
                tf_password_confirm,
                ft.Row(controls=[save_btn, cancel_btn], **EDIT_BUTTON_ROW),
            ],
        ),
    )

    top_card = ft.Container(
        **TOP_CARD,
        content=ft.Row(
            **TOP_CARD_ROW,
            controls=[
                left_panel,
                ft.VerticalDivider(width=1, color=ft.Colors.BLUE_GREY_100),
                right_panel,
            ],
        ),
    )

    banner = ft.Container(
        **BANNER,
        content=ft.Stack(
            expand=True,
            controls=[
                ft.Container(**BANNER_CIRCLE_BIG),
                ft.Container(**BANNER_CIRCLE_SMALL),
                ft.Container(**BANNER_CIRCLE_MID),
                ft.Container(
                    **BANNER_INNER_CONTAINER,
                    content=ft.Column(
                        **BANNER_COLUMN,
                        controls=[
                            ft.Row(
                                **BANNER_ICON_ROW,
                                controls=[
                                    ft.Icon(ft.Icons.PHISHING, **BANNER_ICON),
                                    ft.Text("Рибальський застосунок", **BANNER_TITLE_TEXT),
                                ],
                            ),
                            ft.Text(
                                "Лови більше - записуй кожен улов!",
                                **BANNER_SUBTITLE_TEXT,
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )

    return ft.Column(
        controls=[
            top_card,
            ft.Container(height=16),
            banner,
        ],
        spacing=0,
        expand=True,
    )
