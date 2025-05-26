import requests # type: ignore

def get_weather(api_key, location):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    else:
        print("Error fetching weather data. Please check the city name or API key.")

def main():
    api_key = "6faf8f5928326f2a2358f9cc3f0b1392"  
    location = input("Enter city name: ").strip()
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
