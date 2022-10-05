import cv2 as cv


img = cv.imread('photos/park.jpg')
cv.imshow('Cat', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

# bluring an image
blur = cv.Ga![](photos/face.jpg)ussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#Edge cascade
canny =cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

#dilating the image
dilated = cv.dilate(canny, (7,7), iterations =3)
cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations= 3 )
cv.imshow('eroded', eroded)


# resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
cv.imshow('resized',resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)