#!/usr/bin/env python

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

GREEN_LED = 23

GPIO.setup(GREEN_LED, GPIO.OUT)

while True:
    GPIO.output(GREEN_LED, True)

    time.sleep(1)

    GPIO.output(GREEN_LED, False)

    time.sleep(1)
