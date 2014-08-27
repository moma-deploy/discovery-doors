#!/usr/bin/env python

import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

DOOR_SWITCH = 23

GPIO.setup(DOOR_SWITCH, GPIO.IN)

while True:
    print GPIO.input(DOOR_SWITCH)

    time.sleep(1)
