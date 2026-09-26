import requests

def get_weather(lat, lon):
    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": lat, "longitude": lon, "current_weather": True},
            timeout=5
        )
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print("Error: the request timed out.")
        return
    except requests.exceptions.ConnectionError:
        print("Error: could not connect to the API.")
        return
    except requests.exceptions.HTTPError as e:
        print(f"Error: API returned an HTTP error — {e}")
        return

    try:
        data = response.json()
        temp = data["current_weather"]["temperature"]
        wind = data["current_weather"]["windspeed"]
    except (KeyError, ValueError):
        print("Error: unexpected response format from API.")
        return

    print(f"{'Temperature':15} {temp:>6.1f} °C")
    print(f"{'Wind speed':15} {wind:>6.1f} km/h")

get_weather(13.08, 80.27)