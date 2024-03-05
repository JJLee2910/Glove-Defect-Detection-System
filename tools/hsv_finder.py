import cv2
import numpy as np
def on_change(val):
    pass


img = cv2.imread('C:\\Users\\JJ\\OneDrive\\Desktop\\Glove-Defect-Detection-System\\Images\\Latex\\tear_2.jpg')
img = cv2.resize(img, (500, 500))

ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

windowName = 'image'
cv2.namedWindow(windowName)
cv2.createTrackbar('lowH','image',ilowH,179,on_change)
cv2.createTrackbar('highH','image',ihighH,179,on_change)

cv2.createTrackbar('lowS','image',ilowS,255,on_change)
cv2.createTrackbar('highS','image',ihighS,255,on_change)

cv2.createTrackbar('lowV','image',ilowV,255,on_change)
cv2.createTrackbar('highV','image',ihighV,255,on_change)
while(1):

    ilowH = cv2.getTrackbarPos('lowH', windowName)
    ihighH = cv2.getTrackbarPos('highH', windowName)
    ilowS = cv2.getTrackbarPos('lowS', windowName)
    ihighS = cv2.getTrackbarPos('highS', windowName)
    ilowV = cv2.getTrackbarPos('lowV', windowName)
    ihighV = cv2.getTrackbarPos('highV', windowName)

    img_copy = img.copy()
    img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2LAB)
    upper = np.array([ihighH, ihighS, ihighV])
    lower = np.array([ilowH, ilowS, ilowV])
    img_copy = cv2.inRange(img_copy, lower, upper)
    img_copy = cv2.bitwise_and(img, img, mask=img_copy)
    print(img_copy)

    cv2.imshow(windowName, img_copy)
    cv2.waitKey(500)