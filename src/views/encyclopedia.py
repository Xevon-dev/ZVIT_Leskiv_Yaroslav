import flet as ft


class EncyclopediaView(ft.View):
    def __init__(self):
        super().__init__(
            route="/encyclopedia",
            controls=[
                ft.AppBar(
                    title=ft.Text("Енциколпедія рибака"),

                    leading=ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        on_click=self.go_home
                    ),
                ),

                ft.Divider(),

                ft.Text("Сторінка енцеклопедія")
            ]
        )

    async def go_home(self, e):
        await self.page.push_route("/home")
