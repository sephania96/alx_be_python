# Instruction:
# Use the requests library to fetch weather information from an online weather API (e.g., weatherap
# Install the requests library using pip if it’s not already installed pip install requests.
# Write a Python script weather.py to use the requests.get method to fetch weather data from the API.
# Print out relevant weather information (e.g., temperature, weather description) from the API response.

import requests
baseUrl = "https://api.openweathermap.org/data/2.5/weather?q=Accra,gh&APPID=4988a285bb20f4243e91bb8d92ab7062"

res = requests.get(baseUrl)

print(res.json())
