import cv2
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer
from tools.missing_finger_checker import MissingFingerChecker


class MissingFingerDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img
        self.img = cv2.resize(img, None, fx=0.2, fy=0.2)

    def detect(self):
        try:
            mask = ColorBasedBinarizer.apply(self.img, 0.6, 0.8, 0.1)
            result = MissingFingerChecker.apply(self.img, mask)
        except Exception as e:
            print(e)
            result = None

        cv2.imshow("mask", mask)

        if result is not None:
            cv2.imshow("Combined", result)
        else:
            cv2.imshow("Original Image", self.img)
        cv2.waitKey(0)
