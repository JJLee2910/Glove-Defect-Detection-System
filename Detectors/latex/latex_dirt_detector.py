import cv2
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer
from tools.missingFinger import missingFinger

class DirtDetectors(Detector):
    def __init__(self, img) -> None:
        self.img = img
        self.img = cv2.resize(img, None, fx=0.2, fy=0.2)
        self.masked_img = ColorBasedBinarizer.apply(img, 0.1, 0.2, 0.3)

    def detect(self):
        missingFinger.findMissingFinger(self.img, self.masked_img)
