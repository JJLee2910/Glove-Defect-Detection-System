import cv2
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer


class DirtDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img

    def detect(self):
        # binarize the images
        result = ColorBasedBinarizer.apply(self.img, 0.6, 1.0, 0.15)

        result = StainFinder()

        cv2.imshow("Combined", combined_img)
        cv2.waitKey(0)
