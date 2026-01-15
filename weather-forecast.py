import argparse
import requests
from dotenv import load_dotenv
import os

load_dotenv("api.env")

API_KEY = os.getenv("Key_API")
if not API_KEY:
    raise ValueError("Key_API not found. Please set it in your api.env file.")

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
    try:
        error_data = response.json()
        message = error_data.get("message", "No message provided")
        code = error_data.get("cod", "No code provided")
    except ValueError:
        message = "No message provided"
        code = "No code provided"

    print(f"Error fetching weather for {args.city}:")
    print(f"HTTP Status Code: {response.status_code}")
    print(f"API Error Message: {message}")
    print(f"API Error Code: {code}")
