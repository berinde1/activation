# Chat GPT code (converted code from Python to Micropython)

import urequests
import ujson
import network
import time

# Wi-Fi credentials
SSID = "your_wifi_ssid"
PASSWORD = "your_wifi_password"

# OpenWeatherMap API Key and URL
API_KEY = "79f1a66db32bf4aa923aeec9ac148b2a"
CITY = "Ouarzazate"
URL = f"https://api.openweathermap.org/data/3.0/onecall?lat=30.919&lon=-6.893&exclude=current,minutely,alerts&units=metric&appid=79f1a66db32bf4aa923aeec9ac148b2a"

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    print("Connecting to Wi-Fi...")
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected!")

# Fetch weather data
def get_weather():
    try:
        response = urequests.get(URL)
        weather_data = response.json()
        response.close()

        # Extract necessary data
        wind_speed = weather_data["wind"]["speed"]
        wind_direction = weather_data["wind"]["deg"]

        print(f"Wind speed: {wind_speed} km/h")
        print(f"Wind direction: {wind_direction}°")

    except Exception as e:
        print("Failed to fetch weather:", e)

# Main function
def main():
    connect_wifi()
    while True:
        get_weather()
        time.sleep(600)  # Fetch new data every 10 minutes

# Run the program
main()
