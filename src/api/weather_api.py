import requests


API_KEY = "93939de6fd964b67b96110906262303"
BASE_URL = "http://api.weatherapi.com/v1"

def get_forecast(city: str):
    return requests.get(f"{BASE_URL}/forecast.json?key={API_KEY}&q={city}&days=3&lang=uk").json()


# print(get_forecast(city="Lviv"))

