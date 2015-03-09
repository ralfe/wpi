import logging

import RPi.GPIO as GPIO

__author__ = 'renderle'

logging.basicConfig(filename='/home/renderle/water.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

print("script startWaterHeating.py started")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
logging.info("Start WaterHeating")
GPIO.output(13, GPIO.HIGH)
logging.info("")
print("script startWaterHeating.py stopped - good bye")





