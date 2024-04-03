import cv2
import numpy as np
from Detectors.base import Detector
from tools.new_color_segmenter import ColorBasedSegmenter
from tools.resizer import Resizer
from tools.stain_finder import StainFinder


class DirtDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img

    def detect(self):
        # binarize the images
        result = ColorBasedSegmenter.apply(self.img, 0.65, 1.0, 0.15)

        result = StainFinder().apply(result)

        cv2.imshow("Result", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()