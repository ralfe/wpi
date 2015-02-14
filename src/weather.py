__author__ = 'renderle'

import requests
import json

print("start parsing weather data")

print("----> 1: do request")

url = 'http://api.openweathermap.org/data/2.5/weather'
data = 'q=ulm&units=metric'
response = requests.get(url, params=data)

print()

print("----> 2: WeatherData response")

print("URL :", response.url)
print("status code: ", response.status_code)
print("data ", response.json())

print()

print("----> 3: parsing json")

data = response.json()

main = data['main']

tempMin = main['temp_min']

print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

print()
print()
print("Aktuelle Temperatur Ulm: ", tempMin)






