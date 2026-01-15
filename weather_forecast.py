import argparse
import requests
from dotenv import load_dotenv
import os
def weather_fetch(city, api_key):
    WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    } 
    response = requests.get(WEATHER_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        print(f"Weather in {city}:")
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
        print(f"Error fetching weather for {city}:")
        print(f"API Error Message: {message}")
        print(f"API Error Code: {code}")
def main():
    load_dotenv("api.env")
    API_KEY = os.getenv("Key_API")
    parser = argparse.ArgumentParser(description="Get current weather of a city")
    parser.add_argument("city", help="Name of the city")
    args = parser.parse_args()
    weather_fetch(args.city, API_KEY)
if __name__=="__main__":
    main()