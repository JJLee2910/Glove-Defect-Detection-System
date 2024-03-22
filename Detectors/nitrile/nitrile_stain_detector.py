import cv2
import numpy as np
# from tools.color_based_binarizer import ColorBasedBinarizer
from skimage.color import rgb2hsv

def apply(img, lower_hue, upper_hue, saturation_threshold):
        hsv_image = rgb2hsv(img)

        lower_mask = hsv_image[..., 0] > lower_hue
        upper_mask = hsv_image[..., 0] < upper_hue
        saturation_mask = hsv_image[..., 1] > saturation_threshold

        mask = np.logical_and.reduce((lower_mask, upper_mask, saturation_mask))
        masked_image = img * np.expand_dims(mask, axis=2)

        return masked_image

image = cv2.imread("D:\\OneDrive - Asia Pacific University\\Degree Year 3\\Image Processing, Computer Vision and Pattern Recognition\\Assignment\\Source Code\\Glove-Defect-Detection-System\\Images\\Cloth\\stain_1.jpg")
image = cv2.resize(image, None, fx=0.3, fy=0.3)


# binarize the images
masked_img = apply(image, 0.0, 0.2, 0.05)

# Convert to grayscale
gray = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)       

# Thresholding
ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)  

# Reduce noise
blur = cv2.medianBlur(th,15) 

# Find stain with contour
contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

stainCounter = 0
for contour in contours:
    if (cv2.contourArea(contour) < 5000 and cv2.contourArea(contour) > 20):
        # draw out all the contour
        perimeter = cv2.arcLength(contour,True)
        vertices = cv2.approxPolyDP(contour, perimeter * 0.02, True)
        x, y, w, h = cv2.boundingRect(vertices)
        cv2.rectangle(image, (x,y),(x+w,y+h), (0,0,255),2)

        # Put text on top of the rectangle
        cv2.putText(image, 'Stain', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

        stainCounter = stainCounter + 1 

# Put text to show number of hole detected
cv2.putText(image, 'Stain detected: '+str(stainCounter), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)


cv2.imshow('ori',masked_img)
cv2.imshow('img', blur)
cv2.imshow('img2', image)
cv2.waitKey(0)