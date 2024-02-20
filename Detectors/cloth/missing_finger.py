import cv2 as cv
import numpy as np
import cv2
from skimage.color import rgb2hsv

img = cv2.imread("D:\OneDrive - Asia Pacific University\Degree Year 3\Image Processing, Computer Vision and Pattern Recognition\Assignment\Source Code\Glove-Defect-Detection-System\Images\Cloth\\test1.jpg")
# new_img = cv.resize(img, None, fx=0.5, fy=0.5)

def apply_mask(lower_hue, upper_hue, saturation_threshold):
    hsv_image = rgb2hsv(img)

    lower_mask = hsv_image[..., 0] > lower_hue
    upper_mask = hsv_image[..., 0] < upper_hue
    saturation_mask = hsv_image[..., 1] > saturation_threshold

    mask = np.logical_and.reduce((lower_mask, upper_mask, saturation_mask))
    masked_image = img * np.expand_dims(mask, axis=2)
    return masked_image

masked_image = apply_mask(0.0, 0.2, 0.1) 

# Convert to grayscale
gray = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

# Reduce noise
blur = cv2.GaussianBlur(gray, (7,7), 0)
# Thresholding
ret, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY)

# Find Contours
contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

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
cv2.putText(img, str(cnt), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)

cv2.imshow('final_result',img)

cv2.waitKey(0)