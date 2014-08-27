#!/usr/bin/python

import Tkinter as tk
from PIL import Image, ImageTk
from ttk import Frame, Button, Style
import time

class Example():
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('My Pictures')

		imageFile = "img/image01.jpg"
		self.image1 = ImageTk.PhotoImage(Image.open(imageFile))
		self.image2 = ImageTk.PhotoImage(Image.open("img/image160.jpg"))
		
		w = self.image1.width()
		h = self.image1.height()

		x = 0
		y = 0
		
		self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))
		
		self.panel1 = tk.Label(self.root, image=self.image1)
		self.display = self.image1
		self.panel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
		print "Display image1"
		self.root.after(30000, self.update_image)
		self.root.mainloop()

def update_image(self):
	if self.display == self.image1:
		self.panel1.configure(image=self.image2)
		print "Display image2"
		self.display = self.image2
	else:
		self.panel1.configure(image=self.image1)
		print "Display image1"
		self.display = self.image1
	self.root.after(30000, self.update_image)

def main():
	app = Example()

if __name__ == '__main__':
	main()
	
