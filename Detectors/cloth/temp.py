import cv2
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer

class DirtDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img
        # self.img = cv2.resize(img, None, fx=0.2, fy=0.2)

    def detect(self):
        # binarize the images
        result = ColorBasedBinarizer.apply(self.img,0.08, 0.2, 0.1)

        # Concatenate the original image and the result horizontally
        combined_img = np.hstack((self.img, result))

        cv2.imshow("Combined", combined_img)
        cv2.waitKey(0)