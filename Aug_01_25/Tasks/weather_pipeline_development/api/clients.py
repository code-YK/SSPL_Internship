import requests

class WeatherAPIClient:
    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def fetch_weather(self, city: str) -> dict:
        params = {"key": self.api_key, "q": city}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
