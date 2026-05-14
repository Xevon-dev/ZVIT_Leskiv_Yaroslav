def validate_fish(value: str):
    text = (value or "").strip()

    if not text:
        return "Введіть назву риби"

    allowed_chars = " ,'-"
    for char in text:
        if not char.isalpha() and char not in allowed_chars:
            return "Тільки літери"

    return None


def validate_weight(value: str):
    v = (value or "").strip()
    if not v:
        return "Введіть вагу"
    try:
        float(v.replace(",", "."))
    except ValueError:
        return "Тільки числа (напр. 1.5)"
    return None


def validate_place(value: str):
    v = (value or "").strip()
    if not v:
        return "Введіть місце рибалки"
    return None


def validate_bait(value: str):
    v = (value or "").strip()
    if not v:
        return "Введіть наживку"
    return None


def validate_desc(value: str):
    v = (value or "").strip()
    if v and len(v) > 300:
        return "Максимум 300 символів"
    return None


def validate_weather(value: str):
    if not value:
        return "Оберіть погоду"
    return None