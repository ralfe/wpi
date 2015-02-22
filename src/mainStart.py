import logging

import RPi.GPIO as GPIO

__author__ = 'renderle'

logging.basicConfig(filename='/home/renderle/start.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

print("script mainStart.py started")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
logging.info("Start WP")
GPIO.output(11, GPIO.LOW)
logging.info("")
print("script mainStart.py stopped - good bye")





