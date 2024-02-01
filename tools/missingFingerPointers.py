import cv2
import numpy as np

# Read the input image
image = cv2.imread('C:\\Users\\jangj\\OneDrive\\Desktop\\Glove-Defect-Detection-System\\Images\\Latex\\missing_finger.jpg')
image = cv2.resize(image, None, fx=0.2, fy=0.2)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_color = np.array([89, 20, 145], dtype=np.uint8)
upper_color = np.array([107, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_color, upper_color)
blur = cv2.GaussianBlur(mask, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    for point in approx:
        x, y = point.ravel()
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        print(point)

cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
