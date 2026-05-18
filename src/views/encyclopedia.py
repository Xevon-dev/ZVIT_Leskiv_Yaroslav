from src.element.encyclopedia_element import *
from src.element.bottom_appbar import bottom_app_bar


class EncyclopediaView(ft.View):
    def __init__(self):
        super().__init__(
            route="/encyclopedia",
            padding=0,
            controls=[
                ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Енциколпедія рибака"),
                            leading=ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                on_click=self.go_home
                            ),
                        ),
                        ft.Column(
                            controls=[
                                ft.Divider(),
                                encyclopedia_elements()
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        bottom_app_bar()
                    ]
                )
            ]
        )

    async def go_home(self, e):
        await self.page.push_route("/home")
