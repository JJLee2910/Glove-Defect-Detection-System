import cv2
from sklearn.cluster import KMeans
import numpy as np


image = cv2.imread("D:\\OneDrive - Asia Pacific University\\Degree Year 3\\Image Processing, Computer Vision and Pattern Recognition\\Assignment\\Source Code\\Glove-Defect-Detection-System\\Images\\Nitrile\\hole_5.jpg")
image = cv2.resize(image, None, fx=0.3, fy=0.3)

cv2.imshow('img', image)

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# reduce dimension
new_image = image_hsv.reshape(-1, 3)

# Clustering - KMeans
k_means = KMeans(n_clusters=2, n_init=30)
k_means.fit(new_image)

result = k_means.cluster_centers_[k_means.labels_]
result = result.reshape(image.shape).astype(np.uint8)


# Grayscale 
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

ret, th = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY_INV)

# Reduce noise
blur = cv2.medianBlur(th,9)  

# Eliminate small hole/ noise
opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, np.ones((7,7)))



# Find hole with contour
contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(image, contours, -1, (255, 0, 0), 3)

holeCounter = 0
for contour in contours:
    if (cv2.contourArea(contour) < 20000 and cv2.contourArea(contour) > 20):
        # draw out all the contour
        perimeter = cv2.arcLength(contour,True)
        vertices = cv2.approxPolyDP(contour, perimeter * 0.02, True)
        x, y, w, h = cv2.boundingRect(vertices)
        crop_defect = image[y:y+h,x:x+w]
        cv2.rectangle(image, (x,y),(x+w,y+h), (0,0,255),2)

        # Put text on top of the rectangle
        cv2.putText(image, 'Hole', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
        holeCounter = holeCounter + 1


    print(cv2.contourArea(contour))

cv2.putText(image, 'Hole detected: '+str(holeCounter), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)


cv2.imshow("kmeans",result)
cv2.imshow("blur",blur)
cv2.imshow("opening",opening)

cv2.imshow("th",th)
cv2.imshow("result2",image)
cv2.waitKey(0)


