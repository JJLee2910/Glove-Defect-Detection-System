import cv2 as cv
import numpy as np
import cv2
from skimage.color import rgb2hsv


def empty(v):
    pass

kernel = np.ones((3,3), np.uint8)

kernel2 = np.ones((9,9), np.uint8)

img = cv2.imread("C:\\Users\\JJ\\OneDrive\\Desktop\\Glove-Defect-Detection-System\\Images\\Latex\\missing_finger_2.jpg")
img = cv.resize(img, None, fx=0.3, fy=0.3)
# Reduce noise
img = cv2.GaussianBlur(img, (5,5), 0)

def apply_mask(lower_hue, upper_hue, saturation_threshold):
    hsv_image = rgb2hsv(img)

    lower_mask = hsv_image[..., 0] > lower_hue
    upper_mask = hsv_image[..., 0] < upper_hue
    saturation_mask = hsv_image[..., 1] > saturation_threshold

    mask = np.logical_and.reduce((lower_mask, upper_mask, saturation_mask))
    masked_image = img * np.expand_dims(mask, axis=2)
    # dilate = cv2.dilate(masked_image, kernel, iterations= 1)
    closing = cv2.morphologyEx(masked_image, cv2.MORPH_CLOSE, kernel2)
    cv2.imshow('masked_image',masked_image)
    # cv2.imshow('dilate',dilate)
    cv2.imshow('closing',closing)



cv2.namedWindow('TrackBar')
cv2.resizeWindow('TrackBar', 640, 320)
cv2.createTrackbar('Hue Min', 'TrackBar', 0, 100, empty)
cv2.createTrackbar('Hue Max', 'TrackBar', 0, 100, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 100, empty)

while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')/100
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')/100
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')/100
    apply_mask(h_min,h_max,s_min)
    cv2.waitKey(1)