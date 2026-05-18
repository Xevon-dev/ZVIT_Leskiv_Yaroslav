import datetime
from src.styles.card_styles_notes import *
from src.models.notes_logic import *
from src.element.note_card import build_note_card
from src.data.user_json import read_json, save_json
from src.styles.field_styles import INPUT_FIELD_STYLE
from src.styles.dropdown_note_style import WEATHER_DROPDOWN


def notes_elements(page: ft.Page):
    now = datetime.datetime.now()

    def load_notes():
        data = read_json()
        current_user = data.get("current_user", "")
        for user in data.get("users", []):
            if user["login"] == current_user:
                return user.get("notes", [])
        return []

    def save_notes(notes):
        file_data = read_json()
        current_user = file_data.get("current_user", "")
        for user in file_data.get("users", []):
            if user["login"] == current_user:
                user["notes"] = notes
                break
        save_json(file_data)

    notes = load_notes()

    dd_weather = ft.Dropdown(
        **WEATHER_DROPDOWN,
        dense=True,
        expand=True,
        options=[
            ft.DropdownOption(key="sun", text="Сонячно"),
            ft.DropdownOption(key="cloud", text="Хмарно"),
            ft.DropdownOption(key="rain", text="Дощ"),
            ft.DropdownOption(key="wind", text="Вітряно"),
        ],
    )

    weather_error = ft.Text(value="", visible=False, size=12, color=ft.Colors.RED)

    tf_fish = ft.TextField(label="Риба", expand=True, **INPUT_FIELD_STYLE)
    tf_weight = ft.TextField(label="Вага (кг)", expand=True, **INPUT_FIELD_STYLE)
    tf_place = ft.TextField(label="Місце", expand=True, **INPUT_FIELD_STYLE)
    tf_bait = ft.TextField(label="Наживка", expand=True, **INPUT_FIELD_STYLE)
    tf_desc = ft.TextField(label="Опис", multiline=True, min_lines=2, max_lines=3, expand=True, **INPUT_FIELD_STYLE)

    date_label = ft.Text(value=now.strftime("%d.%m.%Y"), size=14)
    time_label = ft.Text(value=now.strftime("%H:%M"), size=14)

    date_picker = ft.DatePicker(
        value=now,
        locale=ft.Locale("uk", "UA"),
    )
    time_picker = ft.TimePicker(
        value=datetime.time(now.hour, now.minute),
        locale=ft.Locale("uk", "UA"),
    )

    notes_column = ft.Column(spacing=10, expand=True)

    sort_field = {"value": None}
    sort_reverse = {"value": False}

    def get_sort_value(note):
        field = sort_field["value"]
        v = note.get(field, "")
        if field == "weight":
            try:
                v = float(str(v).replace(",", "."))
            except ValueError:
                v = 0.0
        return v

    def refresh_list():
        data = notes[:]
        if sort_field["value"]:
            data.sort(key=get_sort_value, reverse=sort_reverse["value"])
        notes_column.controls = []
        for note in data:
            card = build_note_card(note, on_delete=delete_note, on_edit=edit_note)
            notes_column.controls.append(card)
        page.update()

    def sort_by(field):
        if sort_field["value"] == field:
            sort_reverse["value"] = not sort_reverse["value"]
        else:
            sort_field["value"] = field
            sort_reverse["value"] = False
        refresh_list()

    def sort_by_date(e):
        sort_by("date")

    def sort_by_weight(e):
        sort_by("weight")

    def open_date_picker(e):
        page.show_dialog(date_picker)

    def open_time_picker(e):
        page.show_dialog(time_picker)

    def on_date_change(e):
        if date_picker.value:
            date_label.value = date_picker.value.strftime("%d.%m.%Y")
            page.update()

    def on_time_change(e):
        if time_picker.value:
            time_label.value = str(time_picker.value)[:5]
            page.update()

    date_picker.on_change = on_date_change
    time_picker.on_change = on_time_change

    def clear_form():
        tf_fish.value = ""
        tf_weight.value = ""
        tf_place.value = ""
        tf_bait.value = ""
        tf_desc.value = ""
        dd_weather.value = None

        tf_fish.error = None
        tf_weight.error = None
        tf_place.error = None
        tf_bait.error = None
        tf_desc.error = None

        dd_weather.border_color = None
        dd_weather.label_style = None
        weather_error.visible = False

        date_label.value = now.strftime("%d.%m.%Y")
        time_label.value = now.strftime("%H:%M")

    def delete_note(note):
        notes.remove(note)
        save_notes(notes)
        refresh_list()

    def edit_note(note):
        tf_fish.value = note["fish"]
        tf_weight.value = note["weight"]
        tf_place.value = note["place"]
        tf_bait.value = note["bait"]
        tf_desc.value = note["desc"]
        dd_weather.value = note["weather"]
        date_label.value = note["date"]
        time_label.value = note["time"]
        notes.remove(note)
        save_notes(notes)
        refresh_list()

    def save_note(e):
        tf_fish.error = validate_fish(tf_fish.value)
        tf_weight.error = validate_weight(tf_weight.value)
        tf_place.error = validate_place(tf_place.value)
        tf_bait.error = validate_bait(tf_bait.value)
        tf_desc.error = validate_desc(tf_desc.value)

        has_error = any([
            tf_fish.error,
            tf_weight.error,
            tf_place.error,
            tf_bait.error,
            tf_desc.error,
        ])

        weather_err = validate_weather(dd_weather.value)
        if weather_err:
            dd_weather.border_color = ft.Colors.RED
            dd_weather.label_style = ft.TextStyle(color=ft.Colors.RED)
            weather_error.value = weather_err
            weather_error.visible = True
            has_error = True
        else:
            dd_weather.border_color = None
            dd_weather.label_style = None
            weather_error.visible = False

        if has_error:
            page.update()
            return

        new_note = {
            "fish": tf_fish.value.strip(),
            "weight": tf_weight.value.strip(),
            "place": tf_place.value.strip(),
            "bait": tf_bait.value.strip(),
            "desc": tf_desc.value.strip(),
            "weather": dd_weather.value,
            "date": date_label.value,
            "time": time_label.value,
        }

        notes.append(new_note)
        save_notes(notes)
        clear_form()
        refresh_list()

    refresh_list()

    left = ft.Container(
        **FORM_CONTAINER,
        width=300,
        content=ft.Column(
            spacing=10,
            controls=[
                ft.Text("Запишіть нотатки", **SECTION_TITLE),
                dd_weather,
                weather_error,
                tf_fish,
                tf_weight,
                tf_place,
                tf_bait,
                tf_desc,
                ft.Row(
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Оберіть дату:", **DATE_TIME_TEXT),
                        ft.IconButton(
                            icon=ft.Icons.CALENDAR_MONTH,
                            tooltip="Обрати дату",
                            icon_color=ft.Colors.BLUE_500,
                            on_click=open_date_picker,
                        ),
                        date_label,
                    ],
                ),
                ft.Row(
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text("Оберіть час:", **DATE_TIME_TEXT),
                        ft.IconButton(
                            icon=ft.Icons.ACCESS_TIME,
                            tooltip="Обрати час",
                            icon_color=ft.Colors.BLUE_500,
                            on_click=open_time_picker,
                        ),
                        time_label,
                    ],
                ),
                ft.Button(
                    "Зберегти нотатку",
                    icon=ft.Icons.SAVE,
                    style=SAVE_BUTTON_STYLE,
                    on_click=save_note,
                ),
            ],
        ),
    )

    right = ft.Column(
        expand=True,
        spacing=10,
        controls=[
            ft.Row(
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Сортувати за:", size=14,
                            color=ft.Colors.BLUE_GREY_600,
                            weight=ft.FontWeight.W_500),
                    ft.Button("Датою", **SORT_BUTTON, on_click=sort_by_date),
                    ft.Button("Вагою", **SORT_BUTTON, on_click=sort_by_weight),
                ],
            ),
            ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO,
                controls=[notes_column],
            ),
        ],
    )

    return ft.Row(
        expand=True,
        spacing=20,
        vertical_alignment=ft.CrossAxisAlignment.START,
        controls=[left, right],
    )