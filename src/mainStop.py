from src import openweather
from src import wunderground

__author__ = 'renderle'



wundergroundData = openweather.getData()
openweatherData = wunderground.getData()

print("Aggregated data", wundergroundData + openweatherData)
