import requests
import json


class WeatherConfig:
    def __init__(self):
        with open("config.json", "r") as f:
            data = json.load(f)

            self.city = data["city"]
            self.units = data["units"]
            self.api_key = data["api_key"]

    def show(self):
        print(f"Weather in {self.city} uses {self.units} units")


class WeatherFetcher:
    def __init__(self, config):
        self.config = config

    def fetch(self):
        try:
            response = requests.get(
                "https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": 13.08,
                    "longitude": 80.27,
                    "current_weather": True
                },
                timeout=5
            )

            response.raise_for_status()

            data = response.json()

            return data

        except requests.exceptions.RequestException as e:
            print("API request failed:", e)

    def display(self, data):
        temperature = data["current_weather"]["temperature"]
        weather_code = data["current_weather"]["weathercode"]

        print(f"{self.config.city}: {temperature}°C")
        print(f"Weather code: {weather_code}")


W1 = WeatherConfig()
W1.show()

W2 = WeatherFetcher(W1)

data = W2.fetch()

if data:
    W2.display(data)