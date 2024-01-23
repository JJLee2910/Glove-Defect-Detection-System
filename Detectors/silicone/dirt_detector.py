import cv2
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer

class DirtDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img

    def morph_open(self, img):
        kernel = np.ones((5, 5), np.uint8) 
        result = cv2.dilate(img, kernel, iterations=1)
        result = cv2.erode(result, kernel, iterations=3)
        return result

    def detect(self):

        # binarize the image
        lower_pink = np.array([120, 20, 145])
        upper_pink = np.array([180, 255, 255])

        lower_brown = np.array([0, 20, 145])
        upper_brown = np.array([20, 255, 255])

        ranges = [
            [lower_pink, upper_pink],
            [lower_brown, upper_brown]
        ]

        result = ColorBasedBinarizer.apply(self.img, ranges)

        # morphological operation - opening for denoising
        result = self.morph_open(result)

        # find contour

        # filter contour by size

        # if got big contours means got dirt

        cv2.imshow("orig", self.img)
        cv2.imshow("res", result)
        cv2.waitKey(0)