import numpy as np
import cv2
from skimage.color import rgb2hsv
from color_based_binarizer import ColorBasedBinarizer

img = cv2.imread("C:\\Users\\JJ\\OneDrive\\Desktop\\Glove-Defect-Detection-System\\Images\\Latex\\missing_finger_3.jpg")
img = cv2.resize(img, None, fx=0.2, fy=0.2)

masked_image = ColorBasedBinarizer.apply(img,0.0, 0.2, 0.05) 

# Convert to grayscale
gray = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

# Thresholding
ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)

# Reduce noise
blur = cv2.medianBlur(th,15)
cv2.imshow("th",blur)



# Find Contours
contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Get the largest area of contours
contours = max(contours, key=lambda x: cv.contourArea(x))
cv2.drawContours(img, [contours], -1, (255,0,0), 2)

hull = cv2.convexHull(contours)
cv2.drawContours(img, [hull], -1, (0, 255, 255), 2)

hull = cv2.convexHull(contours, returnPoints=False)
defects = cv2.convexityDefects(contours, hull)
cv2.imshow('hull',img)

if defects is not None:
    cnt = 0
for i in range(defects.shape[0]):  # calculate the angle
    s, e, f, d = defects[i][0]
    start = tuple(contours[s][0])
    end = tuple(contours[e][0])
    far = tuple(contours[f][0])
    a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
    b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
    c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
    angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  #      cosine theorem
    if angle <= np.pi / 2:  # angle less than 90 degree, treat as fingers
        cnt += 1
        cv2.circle(img, far, 4, [0, 0, 255], -1)
if cnt > 0:
    cnt = cnt+1

# Put text to image
cv2.putText(img, str(cnt), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)

cv2.imshow('final_result',img)

cv2.waitKey(0)