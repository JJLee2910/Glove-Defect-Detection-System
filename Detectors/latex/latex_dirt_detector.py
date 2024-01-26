import cv2
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer

class DirtDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img
        self.img = cv2.resize(img, None, fx=0.2, fy=0.2)

    def detect(self):
        # binarize the images
        result = ColorBasedBinarizer.apply(self.img, 0.5, 0.6, 0.4)

        cv2.imshow("orig", self.img)
        cv2.imshow("res", result)
        cv2.waitKey(0)
