import flet as ft


def get_recommendation(wind, precip, pressure):
    lines = []

    if wind > 30:
        lines.append("💨 Сильний вітер - краще не йти на рибалку.")
    elif wind > 15:
        lines.append("💨 Помірний вітер - риба може бути активна біля берега.")
    else:
        lines.append("💨 Вітер слабкий - гарні умови для риболовлі.")

    if precip > 10:
        lines.append("🌧️ Сильний дощ - риба не клює, краще не йти.")
    elif precip > 0:
        lines.append("🌦️ Невеликий дощ - перед дощем кльов зазвичай добрий.")
    else:
        lines.append("☀️ Без опадів - сприятливо для риболовлі.")

    if 750 <= pressure <= 760:
        lines.append("🔵 Тиск стабільний - можливий кльов!")
    elif pressure < 748:
        lines.append("🔵 Тиск низький - риба пасивна, кльов слабкий.")
    else:
        lines.append("🔵 Тиск високий - риба тримається глибини.")

    return "\n\n".join(lines)


local_rec_box = ft.Container(
    visible=False,
    width=420,
    padding=20,
    border_radius=16,
    bgcolor=ft.Colors.WHITE,
    border=ft.Border.all(1, ft.Colors.BLUE_100),
    shadow=ft.BoxShadow(
        blur_radius=12,
        color=ft.Colors.with_opacity(0.1, ft.Colors.BLUE_900),
        offset=ft.Offset(0, 4),
    ),
)
