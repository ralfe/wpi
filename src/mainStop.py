import logging

from src.openweather import openweather
from src.wunderground import wunderground
from src import forecastCalculator

__author__ = 'renderle'

logging.basicConfig(filename='stop.log', level=logging.DEBUG, format='%(asctime)s %(message)s')



# current breakEven value to toggle WP
breakEven = 50;


def breakEvenReachedFor(value):
    return value > breakEven


wundergroundData = openweather.getForecastValue()
openweatherData = wunderground.getForecastValue()

scrambledValue = forecastCalculator.scrambleForecast(wundergroundData, openweatherData)

if breakEvenReachedFor(scrambledValue):
    logging.info("BreakEven reached")
else:
    logging.info("BreakEven not reached")

print("Aggregated data", scrambledValue)




