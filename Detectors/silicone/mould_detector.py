import cv2
import numpy as np
from Detectors.base import Detector
from tools.new_color_segmenter import ColorBasedSegmenter
from tools.resizer import Resizer
from tools.stain_finder import StainFinder


RESULT_IMG_TARGET_HEIGHT = 500
GREEN_LOWER_HUE = 160
GREEN_HIGHER_HUE = 240
GREEN_PIXEL_RATIO_OF_MOULD = 50


class MouldDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img

    def detect(self):
        # binarize the images
        binarized_image = ColorBasedSegmenter.apply(self.img, 0.65, 1.0, 0.15)

        image = cv2.cvtColor(binarized_image, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(image, 15)

        # Remove the largest contour from the list of contours
        contours, _ = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = list(contours)
        largest_contour_index = max(
            range(len(contours)), key=lambda i: cv2.contourArea(contours[i])
        )
        contours.pop(largest_contour_index)

        if len(contours) == 0:
            result = self.mould_not_found(binarized_image)
            cv2.imshow("Result", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return

        # Draw the remaining contours on the original image
        result_image = cv2.drawContours(self.img.copy(), contours, -1, (0, 255, 0), 2)

        for contour in contours:

            # Count green pixels
            green_pixel_num = 0
            for point in contour:
                x, y = point[0]
                hue_value = self.img[y, x, 0]

                if GREEN_LOWER_HUE <= hue_value <= GREEN_HIGHER_HUE:
                    green_pixel_num += 1

            # Calculate green pixel ratio
            ratio = green_pixel_num / len(contour) * 100
            if ratio >= GREEN_PIXEL_RATIO_OF_MOULD:
                result = self.mould_found(result_image)
                cv2.imshow("Result", result)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                return

        binarized_image = Resizer.apply(binarized_image, RESULT_IMG_TARGET_HEIGHT)

        result = self.mould_not_found(result_image)

        cv2.imshow("Result", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def mould_found(self, img):
        cv2.putText(
            img,
            "Mould detected",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
            cv2.LINE_AA,
        )
        return img

    def mould_not_found(self, img):
        cv2.putText(
            img,
            "Mould not detected",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )
        return img
