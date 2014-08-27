#!/usr/bin/env python

import Tkinter as tk
from PIL import Image, ImageTk
import time
import RPi.GPIO as io
import random

# SET UP GPIO STUFF
io.setmode(io.BCM)
door_pin = 23

# SET UP IMAGE STUFF
root = tk.Tk()
root.title('image')

imageFile1 = ImageTk.PhotoImage(Image.open("img/image01.jpg"))
imageFile2 = ImageTk.PhotoImage(Image.open("img/image02.jpg"))

w = 1920 
h = 1080 

x = 0
y = 0

panel1 = ""

root.geometry("%dx%d+%d+%d" %  (w, h, x, y))

io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)

def display_image(n):
	if n == 0:
		print("image01 picked")
		img = imageFile1
	else:
		print("image02 picked")
		img = imageFile2

        global panel1
        if panel1 == "":
	    panel1 = tk.Label(root, image=img)
	    panel1.pack(side='top', fill='both', expand = 'yes')
	    panel1.image = img
        else:
            panel1.configure(image = img)

	root.update()

doorIsOpen = False

while True:
	if io.input(door_pin):
           if doorIsOpen == False:
		print("DOOR OPENED")
                rand = random.randint(0,1)
		display_image(rand)
                doorIsOpen = True

        else:
            if doorIsOpen:
                print("DOOR CLOSED")
                doorIsOpen = False
		
	time.sleep(0.25)
