import argparse
import requests

API_KEY = "60114985e8fa14f79ed6f5e80e302ebd"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

parser = argparse.ArgumentParser(description="Get current weather of a city")
parser.add_argument("city", help="Name of the city")
args = parser.parse_args()

params = {
    "q": args.city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(WEATHER_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]

    print(f"Weather in {args.city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")
else:
    print("City not found or API error")
