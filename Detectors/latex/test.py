import cv2 as cv
import numpy as np

img_path = "C:\\Users\\JJ\\OneDrive\\Desktop\\Glove-Defect-Detection-System\\Images\\Latex\\Dirt_4.jpg"
fixed_size = (500, 500)

# Read the image
img = cv.imread(img_path)

# Resize the image
ori_frame = cv.resize(img, fixed_size, interpolation=cv.INTER_CUBIC)
frame = cv.resize(img, fixed_size, interpolation=cv.INTER_CUBIC)

hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

lower_hsv = np.array([85, 65, 0])
higher_hsv = np.array([103, 255, 255])
mask = cv.inRange(hsv_img, lower_hsv, higher_hsv)

# Apply morphological operations
kernel = np.ones((3, 3), np.uint8)
mask = cv.erode(mask, kernel, iterations=2)
mask = cv.dilate(mask, kernel, iterations=2)

blur = cv.medianBlur(mask, 5)

contours, _ = cv.findContours(blur, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# draw the contour on the img
cv.drawContours(frame, contours, -1, (255, 0, 0), 3)

print(len(contours))

if len(contours) > 1:
    print("Stain found")
    cv.putText(
        frame,
        "Stain detected",
        (0, 50),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
        cv.LINE_AA,
    )
else:
    print("No stain found")
    cv.putText(
        frame,
        "Stain not detected",
        (0, 50),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv.LINE_AA,
    )

cv.imshow("ori", ori_frame)
cv.imshow("result", frame)
cv.imshow("mask", mask)
cv.imshow("blur", blur)
cv.waitKey(0)
cv.destroyAllWindows()
