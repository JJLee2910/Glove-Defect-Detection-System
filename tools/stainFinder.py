import cv2
import numpy as np

# Step 1: Read the image
image = cv2.imread('C:\\Users\\JJ\\OneDrive\\Desktop\\Glove-Defect-Detection-System\\Images\\Latex\\Dirt_2.jpg')
image = cv2.resize(image, None, fx=0.2, fy=.2)

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gry',gray_image)

# Step 3: Apply thresholding to find the gloves
_, threshold = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('th',threshold)

# Step 4: Invert the thresholded image
inverted_threshold = cv2.bitwise_not(threshold)

# Step 5: Find contours
contours, _ = cv2.findContours(inverted_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Step 6: Find the largest contour (which represents the outline of the gloves)
largest_contour = max(contours, key=cv2.contourArea)

# Step 7: Draw the contour of the gloves
cv2.drawContours(image, [largest_contour], -1, (0, 255, 0), 2)

# Step 8: Draw contours of the stains
for contour in contours:
    if contour is not largest_contour:
        cv2.drawContours(image, [contour], -1, (0, 0, 255), 2)

# Step 9: Display the result
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()