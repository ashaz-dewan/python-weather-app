import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    if not API_KEY:
        raise RuntimeError("Set the OPENWEATHER_API_KEY environment variable.")

    response = requests.get(
        BASE_URL,
        params={"q": city, "appid": API_KEY, "units": "metric"},
    )
    status_code = response.status_code
    if status_code == 404:
        raise ValueError(f"City '{city}' not found.")
    if status_code == 401:
        raise RuntimeError("Invalid API key.")
    if status_code != 200:
        raise RuntimeError(f"API error: HTTP {status_code}")

    data = response.json()
    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temp": round(data["main"]["temp"], 1),
        "feels_like": round(data["main"]["feels_like"], 1),
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
    }


def get_mood(condition):
    if condition == "Clear":
        return "sunny"
    if condition == "Clouds":
        return "cloudy"
    if condition in ("Rain", "Drizzle"):
        return "rainy"
    if condition == "Thunderstorm":
        return "stormy"
    if condition == "Snow":
        return "snowy"
    if condition in ("Mist", "Fog", "Haze"):
        return "foggy"
    return "unknown"


if __name__ == "__main__":
    city = input("Enter a city: ")
    try:
        weather = get_weather(city)
        for field, value in weather.items():
            print(f"{field}: {value}")
        print(f"mood: {get_mood(weather['condition'])}")
    except ValueError as error:
        print(error)
    except RuntimeError as error:
        print(error)
