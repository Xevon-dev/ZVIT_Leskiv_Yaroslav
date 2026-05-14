import flet as ft


CHECKBOX_STYLE = {
    "active_color": ft.Colors.BLUE_600,
    "check_color": ft.Colors.WHITE,

    "fill_color": {
        ft.ControlState.DEFAULT: ft.Colors.GREY_100,
        ft.ControlState.HOVERED: ft.Colors.BLUE_50,
        ft.ControlState.SELECTED: ft.Colors.BLUE_600,
    },

    "border_side": {
        ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.BLUE_200),
        ft.ControlState.HOVERED: ft.BorderSide(1.5, ft.Colors.BLUE_400),
        ft.ControlState.SELECTED: ft.BorderSide(1.5, ft.Colors.BLUE_600),
    },

    "shape": ft.RoundedRectangleBorder(radius=6),

    "overlay_color": {
        ft.ControlState.PRESSED: ft.Colors.BLUE_200,
    },
}