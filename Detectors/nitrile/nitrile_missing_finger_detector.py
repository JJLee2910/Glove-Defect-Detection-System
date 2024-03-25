import cv2
import numpy as np
from Detectors.base import Detector
from tools.missing_finger_checker import MissingFingerChecker
from tools.new_color_segmenter import ColorBasedSegmenter

class MissingFingerDetector(Detector):
    def _init_(self, img) -> None:
        self.img = img

    def detect(self):
        self.img = cv2.resize(self.img, None, fx=0.2, fy=0.2)
        # binarize the images
        mask = ColorBasedSegmenter.apply(self.img, 0, 0.2, 0.05)
        result = MissingFingerChecker.apply(self.img, mask)
        
        cv2.imshow("result", result)
        cv2.waitKey(0)