from src.data.fish_dani import FISH_DATA
from src.styles.styles_encyclopedia import *


def encyclopedia_elements():
    rows = []

    for i, fish in enumerate(FISH_DATA):
        image_card = ft.Container(
            **IMAGE_CARD_CONTAINER,
            content=ft.Image(
                src=fish["image"],
                fit=ft.BoxFit.COVER,
                width=380,
                height=200,
                border_radius=12,
            ),
        )

        if i % 2 == 0:
            gradient = ft.LinearGradient(
                begin=ft.Alignment(-1, 0),
                end=ft.Alignment(1, 0),
                colors=[ft.Colors.BLUE_100, ft.Colors.CYAN_50, ft.Colors.WHITE],
            )
        else:
            gradient = ft.LinearGradient(
                begin=ft.Alignment(1, 0),
                end=ft.Alignment(-1, 0),
                colors=[ft.Colors.BLUE_100, ft.Colors.CYAN_50, ft.Colors.WHITE],
            )

        desc_card = ft.Container(
            **DESC_CARD_CONTAINER,
            expand=True,
            gradient=gradient,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text(fish["name"], **FISH_NAME_TEXT),
                    ft.Text(fish["desc"], **FISH_DESC_TEXT),
                ],
            ),
        )

        cards = [image_card, desc_card] if i % 2 == 0 else [desc_card, image_card]

        rows.append(
            ft.Container(
                **ROW_CONTAINER,
                content=ft.Row(controls=cards, spacing=12),
            )
        )

    return ft.Column(
        spacing=0,
        expand=True,
        controls=[
            ft.Container(height=12),
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16),
                content=ft.Text("Риби України", **SECTION_TITLE),
            ),
            ft.Container(height=8),
            *rows,
            ft.Container(height=20),
        ],
    )