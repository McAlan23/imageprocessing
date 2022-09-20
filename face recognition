import cv2
img = cv2.imread('face.jpg')
##img = cv2.resize(img, (320,240))


cv2.imshow('original image', img)
key = cv.waitkey(0) & 0*FileNotFoundError

if key == ord('q'):
    cv2.destroyAllWindows()

elif key == ord('s'):
    cv2.imwrite('face_color.jpg',img)
    cv2.destroyAllWindows()

elif key == ord('g'):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('face_gray.jpg',gray)
    cv2.destroyAllWindows()
elif key ==ord('t'):
    text_image = cv2.putText(img, 'Miracle of OPenCV',(10,30), cv2.FONT_SIMPLEX,1,(255,255,0),3)
    cv2.imwrite('face_text.jpg',text_image)
    cv2.destroyAllWindows()
