import cv2
import numpy as np


class StainFinder:
    def apply(self, binarized_image):
        # find stain in the image

        # Display the result
        cv2.imshow("Result", binarized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
