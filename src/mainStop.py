import logging

from openweather import openweather
from wunderground import wunderground
import forecastCalculator
import RPi.GPIO as GPIO

__author__ = 'renderle'

logging.basicConfig(filename='/home/renderle/stop.log', level=logging.DEBUG, format='%(asctime)s %(message)s')


# current breakEven value to toggle WP
breakEven = 50;

def breakEvenReachedFor(value):
    return value > breakEven

print("script mainStop.py started")

# get weather forceast's
openweatherData = openweather.getForecastValue()
wundergroundData = wunderground.getForecastValue()

# scramble all that values
scrambledValue = forecastCalculator.scrambleForecast(wundergroundData, openweatherData)

# check if we reached the breakeven point
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
if breakEvenReachedFor(scrambledValue):
    logging.info("BreakEven reached - scrambled value was %s", scrambledValue)
    GPIO.output(17, GPIO.HIGH)
else:
    logging.info("BreakEven not reached - scrambled value was %s", scrambledValue)
    GPIO.output(11, GPIO.LOW)

logging.info("---------------------------------------------END-------------------------------------------------------------")
logging.info("")
print("script mainStop.py stopped - good bye")





