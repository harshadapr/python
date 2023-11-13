import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data["main"]["temp"]

city_name = "London"
temperature = get_weather(city_name)
print(f"The current temperature in {city_name} is {temperature}°C.")
