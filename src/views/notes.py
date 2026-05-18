import flet as ft
from src.element.notes_elements import notes_elements
from src.element.bottom_appbar import bottom_app_bar


class NotesView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/notes",
            padding=0,
            controls=[
                ft.Column(
                    expand=True,
                    spacing=0,
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Нотатки"),
                            leading=ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                on_click=self.go_back
                            ),
                        ),
                        ft.Column(
                            controls=[
                                ft.Divider(),
                                notes_elements(page)
                            ],
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                        ),
                        bottom_app_bar()
                    ]
                )
            ]
        )

    async def go_back(self, e):
        await self.page.push_route("/home")
