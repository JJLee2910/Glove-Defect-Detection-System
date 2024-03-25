import cv2
import numpy as np
from Detectors.base import Detector
from tools.new_color_segmenter import ColorBasedSegmenter

class StainDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img
        self.img = cv2.resize(img, None, fx=0.2, fy=0.2)
    def detect(self):
        # binarize the images
        masked_img = ColorBasedSegmenter.apply(self.img, 0, 0.2, 0.05)

        # Convert to grayscale
        gray = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)       

        # Thresholding
        ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)  

        # Reduce noise
        blur = cv2.medianBlur(th,15) 

        # Find stain with contour
        contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        stainCounter = 0
        for contour in contours:
            if (cv2.contourArea(contour) < 20000 and cv2.contourArea(contour) > 20):
                # draw out all the contour
                perimeter = cv2.arcLength(contour,True)
                vertices = cv2.approxPolyDP(contour, perimeter * 0.02, True)
                x, y, w, h = cv2.boundingRect(vertices)
                cv2.rectangle(self.img, (x,y),(x+w,y+h), (0,0,255),2)

                # Put text on top of the rectangle
                cv2.putText(self.img, 'Stain', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)

                stainCounter = stainCounter + 1 

        # Put text to show number of hole detected
        cv2.putText(self.img, 'Stain detected: '+str(stainCounter), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)



        cv2.imshow("result", self.img)
        cv2.waitKey(0)
