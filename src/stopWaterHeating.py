import logging

import RPi.GPIO as GPIO

__author__ = 'renderle'

logging.basicConfig(filename='/home/renderle/water.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

print("script stopWaterHeating.py started")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
logging.info("Stop WaterHeating")
GPIO.output(13, GPIO.LOW)
logging.info("")
print("script stopWaterHeating.py stopped - good bye")





