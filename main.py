import cv2 as cv

# img=cv.imread('photos/office.jpg')

# cv.imshow('office' , img)

# cv.waitKey(0)
#read the videos
capture = cv.VideoCapture('videos/crew.mp4')

while True:
    isTrue,frame= capture.read()
    cv.imshow('videos', frame)

    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.realise()
cv.destroyAllWindows()



