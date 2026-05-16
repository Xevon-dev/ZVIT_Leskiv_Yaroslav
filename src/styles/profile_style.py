import flet as ft

AVATAR_GRADIENT = ft.LinearGradient(
    begin=ft.Alignment(-1, -1),
    end=ft.Alignment(1, 1),
    colors=[ft.Colors.TEAL_400, ft.Colors.BLUE_600],
)

AVATAR_SHADOW = ft.BoxShadow(
    blur_radius=12,
    color=ft.Colors.with_opacity(0.25, ft.Colors.TEAL_700),
    offset=ft.Offset(0, 4),
)

AVATAR_CONTAINER = {
    "width": 80,
    "height": 80,
    "border_radius": 40,
    "gradient": AVATAR_GRADIENT,
    "shadow": AVATAR_SHADOW,
    "alignment": ft.Alignment(0, 0),
}

AVATAR_TEXT = {
    "size": 28,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.WHITE,
}


LEFT_PANEL = {
    "width": 200,
    "padding": ft.Padding.all(20),
}

LEFT_COLUMN = {
    "spacing": 4,
    "horizontal_alignment": ft.CrossAxisAlignment.START,
}

RIGHT_PANEL = {
    "expand": True,
    "padding": ft.Padding.all(24),
}

RIGHT_COLUMN = {
    "spacing": 14,
    "horizontal_alignment": ft.CrossAxisAlignment.START,
}

TOP_CARD = {
    "bgcolor": ft.Colors.WHITE,
    "border_radius": 16,
    "border": ft.Border.all(1, ft.Colors.BLUE_GREY_100),
    "shadow": ft.BoxShadow(
        blur_radius=16,
        color=ft.Colors.with_opacity(0.07, ft.Colors.BLUE_900),
        offset=ft.Offset(0, 4),
    ),
}

TOP_CARD_ROW = {
    "vertical_alignment": ft.CrossAxisAlignment.START,
}

STAT_BOX = {
    "padding": ft.Padding.symmetric(horizontal=16, vertical=10),
    "border_radius": 12,
    "bgcolor": ft.Colors.TEAL_50,
    "border": ft.Border.all(1, ft.Colors.TEAL_100),
}

STAT_ROW = {
    "spacing": 8,
    "vertical_alignment": ft.CrossAxisAlignment.CENTER,
}

STAT_ICON = {
    "color": ft.Colors.TEAL_600,
    "size": 20,
}

LOGIN_TEXT = {
    "size": 18,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_GREY_900,
}

EMAIL_TEXT = {
    "size": 13,
    "color": ft.Colors.BLUE_GREY_500,
}

STAT_TEXT = {
    "size": 13,
    "weight": ft.FontWeight.W_600,
    "color": ft.Colors.TEAL_800,
}

EDIT_TITLE_TEXT = {
    "size": 16,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.BLUE_GREY_800,
}

EDIT_DIVIDER = {
    "color": ft.Colors.BLUE_GREY_100,
}

SAVE_BUTTON_STYLE = ft.ButtonStyle(
    bgcolor=ft.Colors.TEAL_600,
    color=ft.Colors.WHITE,
)

LOGOUT_BUTTON_STYLE = ft.ButtonStyle(
    color=ft.Colors.RED_400,
    icon_color=ft.Colors.RED_400,
)

EDIT_BUTTON_ROW = {
    "spacing": 10,
}

BANNER = {
    "height": 200,
    "border_radius": 16,
    "gradient": ft.LinearGradient(
        begin=ft.Alignment(-1, 0),
        end=ft.Alignment(1, 0),
        colors=[ft.Colors.TEAL_700, ft.Colors.BLUE_600, ft.Colors.INDIGO_500],
    ),
    "shadow": ft.BoxShadow(
        blur_radius=20,
        color=ft.Colors.with_opacity(0.18, ft.Colors.INDIGO_900),
        offset=ft.Offset(0, 6),
    ),
}

BANNER_INNER_CONTAINER = {
    "alignment": ft.Alignment(0, 0),
    "expand": True,
}

BANNER_COLUMN = {
    "horizontal_alignment": ft.CrossAxisAlignment.CENTER,
    "alignment": ft.MainAxisAlignment.CENTER,
    "spacing": 10,
}

BANNER_ICON_ROW = {
    "alignment": ft.MainAxisAlignment.CENTER,
    "spacing": 10,
}

BANNER_ICON = {
    "color": ft.Colors.WHITE,
    "size": 34,
}

BANNER_TITLE_TEXT = {
    "size": 26,
    "weight": ft.FontWeight.BOLD,
    "color": ft.Colors.WHITE,
}

BANNER_SUBTITLE_TEXT = {
    "size": 14,
    "color": ft.Colors.with_opacity(0.85, ft.Colors.WHITE),
    "text_align": ft.TextAlign.CENTER,
    "italic": True,
}

BANNER_CIRCLE_BIG = {
    "width": 220,
    "height": 220,
    "border_radius": 110,
    "bgcolor": ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
    "left": -50,
    "top": -60,
}

BANNER_CIRCLE_SMALL = {
    "width": 150,
    "height": 150,
    "border_radius": 75,
    "bgcolor": ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
    "right": -30,
    "bottom": -40,
}

BANNER_CIRCLE_MID = {
    "width": 80,
    "height": 80,
    "border_radius": 40,
    "bgcolor": ft.Colors.with_opacity(0.06, ft.Colors.WHITE),
    "right": 160,
    "top": -20,
}