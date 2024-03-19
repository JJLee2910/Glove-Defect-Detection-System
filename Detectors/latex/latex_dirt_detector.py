import cv2 as cv
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer
from tools.stain_finder import StainFinder
from tools.resizer import Resizer

class DirtDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img
        self.fixed_size = (500,500)
        self.frame = cv.resize(img, self.fixed_size, fx=0, fy=0, interpolation=cv.INTER_CUBIC)

    def detect(self):
        # binarize the images
        hsv_img = cv.cvtColor(self.frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([85, 65, 0])
        higher_hsv = np.array([103, 255, 255])
        mask = cv.inRange(hsv_img, lower_hsv, higher_hsv)

        # Apply morphological operations
        kernel = np.ones((3, 3), np.uint8)
        mask = cv.erode(mask, kernel, iterations=2)
        mask = cv.dilate(mask, kernel, iterations=2)

        blur = cv.medianBlur(mask, 5)

        contours, _ = cv.findContours(blur, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # draw the contour on the img
        cv.drawContours(self.frame, contours, -1, (255, 0, 0), 3)

        print(len(contours))

        if len(contours) > 1:
            print("Stain found")
            cv.putText(
                self.frame,
                "Stain detected",
                (0, 50),
                cv.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
                cv.LINE_AA,
            )
        else:
            print("No stain found")
            cv.putText(
                self.frame,
                "Stain not detected",
                (0, 50),
                cv.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
                cv.LINE_AA,
            )
        cv.imshow("result", self.frame)
        cv.imshow("mask", mask)
        cv.imshow("blur", blur)
        cv.waitKey(0)
        cv.destroyAllWindows()