import cv2
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer
from tools.missing_finger_checker import MissingFingerChecker

class MissingFingerDetector(Detector):
    def _init_(self, img) -> None:
        self.img = img
        # self.img = cv2.resize(img, None, fx=0.2, fy=0.2)
    def detect(self):
        # binarize the images
        mask = ColorBasedBinarizer.apply(self.img,0.0, 0.2, 0.05)
        result = MissingFingerChecker.apply(self.img,mask)
        
        if (result is not None):
            cv2.imshow("Combined", result)
        else:
            cv2.imshow(self.img)
        cv2.waitKey(0)