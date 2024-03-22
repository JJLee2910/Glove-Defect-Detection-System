import cv2
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer
from tools.missing_finger_checker import MissingFingerChecker

class MissingFingerDetector(Detector):
    def _init_(self, img) -> None:
        self.img = img
        self.img = cv2.resize(img, None, fx=0.2, fy=0.2)
    def detect(self):
        # binarize the images
        mask = ColorBasedBinarizer.apply(self.img, 85, 130, 10)
        result = MissingFingerChecker.apply(self.img,mask)
        
        cv2.imshow("result", result)
        cv2.waitKey(0)