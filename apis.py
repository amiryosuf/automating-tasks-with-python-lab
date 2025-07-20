# APIs (Application Programming Interfaces) are like bridges that allow different software systems to talk to each other. 
# Automating with APIs opens up a world of possibilities, from retrieving data to controlling remote services.

# Weather data retriever: Use a weather API (for example, OpenWeatherMap) to fetch current weather conditions for a given city and print the temperature, humidity, and wind speed. 
# Experiment with different API parameters (for example, units or forecast)."

import requests

def get_weather(city, api_key):
    """Fetches current weather data for a specified city using the OpenWeatherMap API."""
    params = {
        'q': city,
        'appid': api_key,  # Your OpenWeatherMap API key
        'units': 'metric'  # Metric units for temperature in Farenheight and wind speed in m/s
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"🌤 Weather in {city}:")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("❌ Failed to retrieve weather data. Check the city name or API key.")

if __name__ == "__main__":
        # Replace with your actual OpenWeatherMap API key
        API_KEY = "e7025382dd7fae7efe5a8d5c419bd7c3"
        city = input("Enter a city name: ")
        get_weather(city, API_KEY)