#RK
import os
import cv2
import numpy as np
from PIL import Image
#importing all the necessary libraries. OS is not too import, however.

#Extrating dimentions of the image
im = Image.open('ImToPix.png')
im = im.convert('1') # converting image to B&W

width, height = im.size
print(width) 
print(height)


#Using openCV to process/read the image ---> unecessary/redundant
#img = im.read()#'ImToPix.png',cv2.IMREAD_COLOR)

xcord =[]
ycord =[]


##this piece of code extracts coordinates based on its coloe value
for y in range(0,height):
	row = ""
	for x in range(0,width):
		RGB = im.getpixel((x,y))
		if RGB == 255:
			xcord.append(x)
			ycord.append(y) #each integer added to y coordinates to its 
					# x integeter in xcord array
		#white will output 255
		#black outputs 0

#This is a test case which check to see if the above piece of code 
#has the correct coordinates. If it does then, black is changed to white
#and vice-versa
def TestCase (im):
	newim=[] #since image is also an array, new array is formed to 
	#store new image array
	white = (255,255,255)
	black = (0,0,0)
	for color in im.getdata(): #getdata() extracts color of each pixel
		if color == 0:
			#print(color,"1")
			color = white
			print("white:", white)
			newim.append(255) 
		else:
			#print(color,"2")
			color = black
			print("black:", black)
			newim.append(0)

		#print(color)

	newimg = Image.new(im.mode, im.size) #new image create, although empty
	newimg.putdata(newim)#data from new array is transfered into new empty image
	return newimg #returning the image

TestCase(im).save( 'imtopixTest1.jpg')#saving the image as imtopixTest.jpg

print(xcord, ycord)





