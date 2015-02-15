import logging

from openweather import openweather
from wunderground import wunderground
import forecastCalculator

__author__ = 'renderle'

logging.basicConfig(filename='stop.log', level=logging.DEBUG, format='%(asctime)s %(message)s')


# current breakEven value to toggle WP
breakEven = 50;

def breakEvenReachedFor(value):
    return value > breakEven

print("script mainStop.py started")

# get weather forceast's
wundergroundData = openweather.getForecastValue()
openweatherData = wunderground.getForecastValue()

# scramble all that values
scrambledValue = forecastCalculator.scrambleForecast(wundergroundData, openweatherData)

# check if we reached the breakeven point
if breakEvenReachedFor(scrambledValue):
    logging.info("BreakEven reached - scrambled value was %s", scrambledValue)
else:
    logging.info("BreakEven not reached - scrambled value was %s", scrambledValue)

logging.info("---------------------------------------------END-------------------------------------------------------------")
logging.info("")
print("script mainStop.py stopped - good bye")





