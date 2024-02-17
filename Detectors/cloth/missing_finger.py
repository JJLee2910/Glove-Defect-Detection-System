import cv2 as cv
import numpy as np
import cv2
from skimage.color import rgb2hsv

img = cv2.imread("C:\\Users\\JJ\\OneDrive\\Desktop\\Glove-Defect-Detection-System\\Images\\Cloth\\test1.jpg")
# new_img = cv.resize(img, None, fx=0.5, fy=0.5)

def apply_mask(lower_hue, upper_hue, saturation_threshold):
    hsv_image = rgb2hsv(img)

    lower_mask = hsv_image[..., 0] > lower_hue
    upper_mask = hsv_image[..., 0] < upper_hue
    saturation_mask = hsv_image[..., 1] > saturation_threshold

    mask = np.logical_and.reduce((lower_mask, upper_mask, saturation_mask))
    masked_image = img * np.expand_dims(mask, axis=2)
    cv2.imshow("masked image",masked_image)
    cv2.waitKey(0)

apply_mask(0.0, 0.2, 0.1) # adjust accordingly based on ur 