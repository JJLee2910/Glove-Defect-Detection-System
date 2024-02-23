import cv2 as cv
import numpy as np
from skimage.color import rgb2hsv
from tools.color_based_binarizer import ColorBasedBinarizer

class missingFinger:
    @staticmethod
    def findMissingFinger(ori_img, masked_img):
        masked_img = ColorBasedBinarizer.apply(ori_img, 0.0,0.2,0.05)

        gray = cv.cvtColor(masked_img, cv.COLOR_BGR2GRAY)

        ret, th = cv.threshold(gray, 0,255,cv.THRESH_BINARY)

        # reduce noise
        blur = cv.medianBlur(th, 15)

        # Find Contours
        contours, hierarchy = cv.findContours(blur, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Get the largest area of contours
        contours = max(contours, key=lambda x: cv.contourArea(x))
        cv.drawContours(ori_img, [contours], -1, (255,0,0), 2)

        hull = cv.convexHull(contours)
        cv.drawContours(ori_img, [hull], -1, (0, 255, 255), 2)

        hull = cv.convexHull(contours, returnPoints=False)
        defects = cv.convexityDefects(contours, hull)

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
                cv.circle(ori_img, far, 4, [0, 0, 255], -1)
        if cnt > 0:
            cnt = cnt+1

        # Put text to image
        cv.putText(ori_img, str(cnt), (0, 50), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv.LINE_AA)
        cv.imshow('final_result',ori_img)
        cv.waitKey(0)