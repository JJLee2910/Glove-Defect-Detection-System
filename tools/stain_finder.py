import cv2
import numpy as np


class StainFinder:
    def apply(self, binarized_image):
        image = cv2.cvtColor(binarized_image, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(image,15)

        contours, _ = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # draw the contour on the img
        cv2.drawContours(binarized_image, contours, -1, (255, 0, 0), 3)
        
        print(len(contours))

        if len(contours) > 1:
            print("Stain found")
            cv2.putText(binarized_image, 'Stain detected', (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255) , 2, cv2.LINE_AA)
        else:
            print("No stain found")
            cv2.putText(binarized_image, 'Stain not detected', (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 0) , 2, cv2.LINE_AA)

        return binarized_image
