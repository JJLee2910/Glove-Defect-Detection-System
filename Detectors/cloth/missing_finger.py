import cv2
import numpy as np
from skimage.color import rgb2hsv


def cApply(img, lower_hue, upper_hue, saturation_threshold):
    hsv_image = rgb2hsv(img)

    lower_mask = hsv_image[..., 0] > lower_hue
    upper_mask = hsv_image[..., 0] < upper_hue
    saturation_mask = hsv_image[..., 1] > saturation_threshold

    mask = np.logical_and.reduce((lower_mask, upper_mask, saturation_mask))
    masked_image = img * np.expand_dims(mask, axis=2)

    return masked_image

def apply(ori_img, masked_img):
    # Convert to grayscale
    gray = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)       

    # Thresholding
    ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)  

    # Reduce noise
    blur = cv2.medianBlur(th,15)  

    # Find Contours
    contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Get the largest area of contours
    contours = max(contours, key=lambda x: cv2.contourArea(x))
    cv2.drawContours(ori_img, [contours], -1, (255,0,0), 2)

    hull = cv2.convexHull(contours)
    cv2.drawContours(ori_img, [hull], -1, (0, 255, 255), 2)

    hull = cv2.convexHull(contours, returnPoints=False)
    defects = cv2.convexityDefects(contours, hull)

    
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
            cv2.circle(ori_img, far, 4, [0, 0, 255], -1)

    # Put text to image
    if cnt >= 4:
        return None
    else:
        cv2.putText(ori_img, 'Missing finger found: '+str(4-cnt), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)
        return ori_img



img = cv2.imread("D:\OneDrive - Asia Pacific University\Degree Year 3\Image Processing, Computer Vision and Pattern Recognition\Assignment\Source Code\Glove-Defect-Detection-System\Images\Cloth\\missing_finger_1.jpg")
img = cv2.resize(img, None, fx=0.3, fy=0.3)

masked_image = cApply(img,0.0,0.2,0.05)
missing = apply(img,masked_image)

if missing is not None:
    cv2.imshow('missing',missing)
    cv2.waitKey(0)
else:
    print("hi")

