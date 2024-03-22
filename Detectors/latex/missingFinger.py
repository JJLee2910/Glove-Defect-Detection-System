import cv2
import numpy as np
from Detectors.base import Detector
from tools.new_color_segmenter import ColorBasedSegmenter
from tools.missing_finger_checker import MissingFingerChecker


class MissingFingerDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img
        self.img = cv2.resize(img, None, fx=0.2, fy=0.2)

    def detect(self):
        try:
            mask = ColorBasedSegmenter.apply(self.img,  0.1, 0.2, 0.3)
            result = MissingFingerChecker.apply(self.img, mask)
        except Exception as e:
            print(e)
            result = None

        cv2.imshow("mask", mask)
        cv2.imshow("Combined", result)
        cv2.waitKey(0)
