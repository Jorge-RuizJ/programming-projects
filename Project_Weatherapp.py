#Jorge Ruiz Jaquez
#Project Assignment - weather app with gui

# This program is a Weather App using the OpenWeatherMap API to input a city,
# and output current weather. Also the program will have temperature conversion 
# included. We will be using tkinter for GUI purposes.

#Reminders:  Code should have at least one class.

import requests
import tkinter as tk

# class section
# This class will handle the call to the api 

class WeatherAPI:
    def __init__(self,city, key):
        self.city = city
        self.key = key
    
    def weather_api_call(self):
        api_url = "http://api.openweathermap.org/data/2.5/weather"
        # parameters that will be applied
        params = {
            "q": self.city,     # api will handle spaces and stuff so we dont need to worry about it
            "appid": self.key,
            "units": "metric"
        }
        #making the call
        response = requests.get(api_url,params=params)

        # only if the connection is established
        if response.status_code == 200:
            return response.json()
        else:
            return None


def weather_info():
    city_name = entry.get() # gets information from the entry box in the app

    # if no input from entry box added
    if not city_name:
        return information.config(text="Please enter a city name.") # config can change the text in gui
    
    city_name = city_name.lower().title().strip() #.title capitalizes first letter

    api_key = "" 

    # calling class and class function (call the api)
    weather = WeatherAPI(city_name,api_key)
    data = weather.weather_api_call()

    if data is None:
        return information.config(text="Error gettting data. Retry entering city name.")
    
    # tapping into the json information, all available in the openweatherapp website
    temp = data['main']['temp']
    temp_fahrenheit = celcius_to_fahrenheit(temp)
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']

    #set an output text to change the text in the gui later
    output_text = (
        f'Weather for {city_name}\n'
        f"Weather: {description}\n"
        f"Temperature: {temp:.1f} Celcius / {temp_fahrenheit:.1f} Fahrenheit\n"
        f"Humidity: {humidity}%"
    )
    #return a change in the gui information box
    return information.config(text=output_text)


#Need functions to convert temperature.
def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * (9 / 5)) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celcius = (fahrenheit - 32) * (5 / 9)
    return celcius

# Tkinter Section
# Things i need to include in this program:
# I need to add an input so the user can input the name of the city. (If there is a space in city name,
# then i need to account for that) (do a strip and split??)
# I need to add Weather description, temperature, maybe humidity, go for all the details i can get.
# For each one i need to update, make the weather data into a class, and then go from there

root = tk.Tk()  #set up
root.geometry("350x400") # size of the window at start
root.title("API Weather App") #title for the app

# Text title inside window
label = tk.Label(root, text="API Weather App", font=("Arial", 14))
label.pack(pady=20) # pady is vertical padding (space)

# Need some instructions for the user
instruction_text = "Please input the name of a city and press 'Get Weather!' to get weather information in that city."
instructions = tk.Label(root, text=instruction_text, wraplength=350) # grap makes sure text doesn't go beyond pixel limit (go outside)
instructions.pack(pady=5)

# Need an entry box for the user to input the city name into the program
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.focus_set()

# Need a button that will start up the program that will fetch weather
button = tk.Button(root, text="Get Weather!", command=weather_info) # need weather command
button.pack(pady=10)

# Info below the entry box which displays weather information
information = tk.Label(root, text="",wraplength=350)
information.pack(pady=10)
root.mainloop() #starts the window

"""
References: 
https://openweathermap.org/weather-data "This reference gives some json stuff along with units."
https://docs.python.org/3/library/tkinter.html "Tkinter Reference: lots of info"
https://requests.readthedocs.io/en/latest/ "more info on requests"

"""

