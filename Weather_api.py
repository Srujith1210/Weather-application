import tkinter as tk
from tkinter import messagebox
import requests

# Replace 'your_api_key' with your actual OpenWeatherMap API key
API_KEY = 'b7390f8f77e838077a0a36a865450e55'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city):
    """Fetch weather data from OpenWeatherMap."""
    complete_url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    return data

def show_weather():
    """Display weather information in the GUI."""
    city = city_entry.get()
    data = get_weather(city)

    
    
    if data['cod'] != '404':
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']
        
        result_text = (
            f"Temperature: {temperature}°C\n"
            f"Pressure: {pressure} hPa\n"
            f"Humidity: {humidity}%\n"
            f"Description: {description.capitalize()}"
        )
        result_label.config(text=result_text)
    else:
        messagebox.showerror("Error", "City not found!")

# Setup Tkinter GUI
root = tk.Tk()
root.title("Weather Application")

# Create and place widgets
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=5)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", command=show_weather)
search_button.pack(pady=5)

result_label = tk.Label(root, text="", padx=10, pady=10)
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
