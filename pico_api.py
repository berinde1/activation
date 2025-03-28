# Chat GPT code (converted code from Python to Micropython)

import urequests
import ujson
import network
import time

# Wi-Fi credentials
SSID = "your_wifi_ssid"
PASSWORD = "your_wifi_password"

# OpenWeatherMap API Key and URL
API_KEY = "your_openweathermap_api_key"
CITY = "Ouarzazate"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

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
