import flet as ft
# from src.element.profile_elements import profile_elements
from src.element.bottom_appbar import bottom_app_bar


class ProfileView(ft.View):
    def __init__(self, page):
        super().__init__(
            route="/profile",
            controls=[
                ft.AppBar(
                    title=ft.Text("Профіль"),

                    leading=ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        on_click=self.go_home
                    ),
                ),
                ft.Column(
                    controls=[
                        ft.Divider(),

                    ],
                    expand=True,
                ),
                bottom_app_bar()
            ]
        )

    async def go_home(self, e):
        await self.page.push_route("/home")
