import cv2
import numpy as np
from tools.color_based_binarizer import ColorBasedBinarizer


class DirtDetector:
    def __init__(self, img) -> None:
        self.img = cv2.resize(img, None, fx=0.2, fy=0.2)

    def morphEx(self, img):
        kernel = np.ones((5, 5), np.uint8) 
        result = cv2.dilate(img, kernel, iterations=1)
        result = cv2.erode(result, kernel, iterations=3)
        return result

    def detect(self):
        # binarize the image
        lower_blue = np.array([89, 20, 145])
        upper_blue = np.array([107, 255, 255])

        ranges = [
            [lower_blue, upper_blue]
        ]

        result = ColorBasedBinarizer.apply(self.img, ranges)

        # morphological operation - opening for denoising
        result = self.morphEx(result)

        # find contour

        # filter contour by size

        # if got big contours means got dirt

        cv2.imshow("orig", self.img)
        cv2.imshow("res", result)
        cv2.waitKey(0)
