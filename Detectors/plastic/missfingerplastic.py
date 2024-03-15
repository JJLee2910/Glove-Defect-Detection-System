import math
import cv2 as cv
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer
from tools.missing_finger_checker import MissingFingerChecker


class MissingFingerDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img

    def detect(self):
        try:
            mask = ColorBasedBinarizer.apply(self.img, 0.65, 1.0, 0.15)

            grey = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
            value = (11, 11)
            blurred_ = cv.GaussianBlur(grey, value, 0)

            contours, hierarchy = cv.findContours(blurred_.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
            count1 = max(contours, key=lambda x: cv.contourArea(x))
            hull = cv.convexHull(count1)
            drawing = np.zeros(mask.shape, np.uint8)
            cv.drawContours(drawing, [hull], 0, (0, 0, 255), 0)
            hull = cv.convexHull(count1, returnPoints=False)
            defects = cv.convexityDefects(count1, hull)

            count_defects = 0
            cv.drawContours(blurred_, contours, -1, (0, 255, 0), 3)

            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(count1[s][0])
                end = tuple(count1[e][0])
                far = tuple(count1[f][0])
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

                if angle <= 90:
                    count_defects += 1
                    cv.circle(mask, far, 1, [0, 0, 255], -1)

                cv.line(mask, start, end, [0, 255, 0], 2)

            finger_count = count_defects + 1
            if finger_count == 5:
                cv.putText(mask, "Missing Finger Not Detected", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
            else:
                cv.putText(mask, "Missing Finger Detected", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))
                cv.putText(mask, f"No. of Fingers: {finger_count}", (50, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0))

        except Exception as e:
            print(e)
            result = None

        cv.imshow("mask", mask)

        cv.waitKey(0)
