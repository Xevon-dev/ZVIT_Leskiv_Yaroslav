import json
import os

USER_DANI = "data/user.json"

def save_json(data: dict):
    with open(USER_DANI, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read_json():
    if os.path.exists(USER_DANI):
        with open(USER_DANI, "r", encoding="utf-8") as file:
            return json.load(file)
    return {
        "user_authorized": False,
        "current_user": "",
        "users": []
    }