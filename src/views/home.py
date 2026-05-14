
from src.data.user_json import *
from src.element.elementes_home import *
from src.element.bottom_appbar import *
from src.styles.button_styles import NAV_BUTTON_STYLE


class HomeView(ft.View):
    def __init__(self):

        dani = read_json()
        is_auth = dani.get("user_authorized", False)
        current_user = dani.get("current_user", "")

        if is_auth and current_user:
            app_title = ft.Column(
                controls=[
                    ft.Text(
                        "Рибальський застосунок",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_GREY_900,
                    ),
                    ft.Text(
                        f"Ласкаво просимо, {current_user}!",
                        size=14,
                        color=ft.Colors.TEAL_600,
                        weight=ft.FontWeight.W_500,
                    ),
                ],
                spacing=3,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        else:
            app_title = ft.Text(
                "Рибальський застосунок",
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_GREY_900,
            )

        super().__init__(
            route="/home",
            controls=[
                ft.Column(
                    controls=[
                        ft.AppBar(
                            leading=ft.IconButton(
                                icon=ft.Icons.MENU,
                                icon_color=ft.Colors.TEAL_600,
                                on_click=self.open_drawer,
                            ),
                            title=app_title,
                            bgcolor=ft.Colors.WHITE,
                            actions=[
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            "Профіль",
                                            style=NAV_BUTTON_STYLE,
                                            on_click=self.go_profile,
                                        ),
                                        ft.ElevatedButton(
                                            "Нотатки рибака",
                                            style=NAV_BUTTON_STYLE,
                                            on_click=self.go_to_login,
                                        ),
                                        ft.ElevatedButton(
                                            "Прогноз кльову",
                                            style=NAV_BUTTON_STYLE,
                                            on_click=self.go_to_fishing_weather,
                                        ),
                                        ft.ElevatedButton(
                                            "Енциклопедія",
                                            style=NAV_BUTTON_STYLE,
                                            on_click=self.go_encyclopedia,
                                        ),
                                    ],
                                    spacing=10,
                                )
                            ],
                        ),

                        ft.Column(
                            controls=[
                                ft.Divider(color=ft.Colors.TEAL_100),
                                element_home(),
                            ],
                            expand=True,
                        ),
                        bottom_app_bar()
                    ],
                )
            ]
        )

    async def open_drawer(self, e):
        self.page.drawer = ft.NavigationDrawer(
            on_change=self.drawer_change,
            controls=[
                ft.Container(height=20),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME,
                    label="Головна",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.PERSON_OUTLINED,
                    label="Профіль",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.BOOK_OUTLINED,
                    label="Нотатки",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.WATER_OUTLINED,
                    label="Прогноз кльову",
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.BOOKMARK_OUTLINED,
                    label="Енциклопедія рибака",
                ),
            ]
        )
        await self.page.show_drawer()

    async def drawer_change(self, e):
        index = e.control.selected_index
        await self.page.close_drawer()

        if index == 0:
            await self.page.push_route("/home")

        elif index == 1:
            dani = read_json()
            if dani["user_authorized"]:
                await self.page.push_route("/profile")
            else:
                self.page.show_dialog(
                    ft.AlertDialog(
                        title=ft.Text("Потрібно увійти"),
                        content=ft.Text("Увійдіть в акаунт для доступу до профілю"),
                        actions=[
                            ft.TextButton("Увійти", on_click=self.go_to_login_or_register)
                        ],
                        open=True,
                    )
                )

        elif index == 2:
            dani = read_json()
            if dani["user_authorized"]:
                await self.page.push_route("/notes")
            else:
                self.page.show_dialog(
                    ft.AlertDialog(
                        title=ft.Text("Потрібно увійти"),
                        content=ft.Text("Увійдіть в акаунт для доступу до нотаток"),
                        actions=[
                            ft.TextButton("Увійти", on_click=self.go_to_login_or_register)
                        ],
                        open=True,
                    )
                )

        elif index == 3:
            await self.page.push_route("/fishing_weather")

        elif index == 4:
            await self.page.push_route("/encyclopedia")

    async def go_to_login(self, e):
        dani = read_json()
        if dani["user_authorized"]:
            await self.page.push_route("/notes")
        else:
            self.page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Потрібно увійти"),
                    content=ft.Text("Увійдіть в акаунт для доступу до нотаток"),
                    actions=[
                        ft.TextButton("Ок", on_click=self.go_to_login_or_register)
                    ],
                    open=True,
                )
            )

    async def go_to_login_or_register(self, e):
        await self.page.push_route("/login")

    async def go_profile(self, e):
        dani = read_json()
        if dani["user_authorized"]:
            await self.page.push_route("/profile")
        else:
            self.page.show_dialog(
                ft.AlertDialog(
                    title=ft.Text("Потрібно увійти"),
                    content=ft.Text("Увійдіть в акаунт для доступу до профілю"),
                    actions=[
                        ft.TextButton("Увійти", on_click=self.go_to_login_or_register)
                    ],
                    open=True,
                )
            )

    async def go_to_fishing_weather(self, e):
        await self.page.push_route("/fishing_weather")

    async def go_encyclopedia(self, e):
        await self.page.push_route("/encyclopedia")
