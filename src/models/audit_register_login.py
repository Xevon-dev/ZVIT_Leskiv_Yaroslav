import re

def valid_email(email):
    template = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(template , email):
        return True

    return False


def audit_parol_letters(parol):
    template_letters = r"[a-zA-Z]"
    return re.search(template_letters , parol)

def audit_parol_numbers(parol):
    template_numbers= r"\d"
    return re.search(template_numbers, parol)






