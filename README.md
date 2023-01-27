# -Python-script-that-retrieves-data-from-an-API


import requests

# Enter your API key
api_key = "YOUR_API_KEY"

# Enter the city name
city_name = "New York"

# Send the API request
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
response = requests.get(url)

# Get the JSON data from the response
data = response.json()

# Get the temperature in Celsius
temperature = data["main"]["temp"] - 273.15

# Get the weather description
description = data["weather"][0]["description"]

# Print the data in a user-friendly format
print(f"Temperature in {city_name}: {temperature:.2f} °C")
print(f"Weather: {description}")



You have to use your own api_key to access OpenWeather API.
You can get it from https://openweathermap.org/ by creating an account and then getting the api_key.
You can modify the city_name to your desired city name.
This script will print the temperature in Celsius and the weather description for the given city.
