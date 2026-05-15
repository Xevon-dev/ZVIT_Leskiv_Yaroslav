import flet as ft
from src.data.fish_dani import FISH_DATA
from src.styles.styles_encyclopedia import *


def encyclopedia_elements():
    rows = []

    for i, (name, desc) in enumerate(FISH_DATA.items()):
        image_card = ft.Card(
            elevation=3,
            content=ft.Container(
                **IMAGE_CARD_CONTAINER,
                content=ft.Icon(ft.Icons.WATER, **IMAGE_CARD_ICON),
            ),
        )

        desc_card = ft.Card(
            elevation=3,
            expand=True,
            content=ft.Container(
                **DESC_CARD_CONTAINER,
                content=ft.Column(
                    spacing=10,
                    controls=[
                        ft.Text(name, **FISH_NAME_TEXT),
                        ft.Text(desc, **FISH_DESC_TEXT),
                    ],
                ),
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
                padding=ft.padding.symmetric(horizontal=16),
                content=ft.Text("Риби України", **SECTION_TITLE),
            ),
            ft.Container(height=8),
            *rows,
            ft.Container(height=20),
        ],
    )