#!/usr/bin/env/python

import os, time
import RPi.GPIO as io
import psutil

io.setmode(io.BCM)
door_pin = 23
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

os.system('feh img/image01.jpg &')

time.sleep(1)

os.system('feh img/image02.jpg &')

time.sleep(2)

def hide_image(image_name):
    for proc in psutil.process_iter():
        cmdline = proc.cmdline()
        if (len(cmdline) > 1) and (cmdline[1] == image_name):
            proc.kill()

hide_image('img/image01.jpg')

time.sleep(2)

hide_image('img/image02.jpg')
