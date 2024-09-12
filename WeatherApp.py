import tkinter as tk
try:
    import requests
except ImportError:
    print("Please install the 'requests' module.")
import json

def get_weather(city, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    weather_data = json.loads(response.text)
    return weather_data

def display_weather(weather_data):
    weather_label.config(text=f"Weather in {weather_data['name']}:")
    temp_label.config(text=f"Temperature: {weather_data['main']['temp']}K")
    humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
    wind_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s")

def search_weather():
    city = city_entry.get()
    api_key = "69605ea17d8a4689f96c3e215223c347"
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

search_button = tk.Button(root, text="Search", command=search_weather)
search_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()
temp_label = tk.Label(root, text="")
temp_label.pack()
humidity_label = tk.Label(root, text="")
humidity_label.pack()
wind_label = tk.Label(root, text="")
wind_label.pack()

root.mainloop()