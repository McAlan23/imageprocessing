import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)
blank = np.zeros((500,1000,3), dtype='uint8')
cv.imshow('Blank',blank)



#1. point the image a certain color

blank[200:300, 200:300]=0,255,0
cv.imshow('Green', blank)

#2. wraw a rectangle throuth the blank imgae

cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = -1)
cv.imshow('Rectangle', blank)

#3.drawing a circle in the blank

#4 draw a line
cv.line(blank, (200,100), (300,400), (0,255,0), thickness = 1)
cv.imshow('Line', blank)

#5. typing a text
cv.putText(blank, 'Hello, MY name is jason', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0 , (200,200,200), 2)
cv.imshow('Text', blank)


cv.waitKey(0)