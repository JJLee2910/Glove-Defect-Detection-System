import cv2
import numpy as np
from sklearn.cluster import KMeans
from Detectors.base import Detector

class HoleDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img
        self.img = cv2.resize(img, None, fx=0.3, fy=0.3)
    def detect(self):
        # convert image to hsv colour space
        image_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

        # reduce dimension
        new_image = image_hsv.reshape(-1, 3)

        # Clustering - KMeans
        k_means = KMeans(n_clusters=2, n_init=30)
        k_means.fit(new_image)

        # get the clustering result
        result = k_means.cluster_centers_[k_means.labels_]
        result = result.reshape(self.img.shape).astype(np.uint8)

        # Convert to grayscale
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

        # Binarize image
        ret, th = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY_INV)

        # Reduce noise
        blur = cv2.medianBlur(th,9)  

        # Eliminate small hole/ noise
        opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, np.ones((7,7)))


        # Find hole with contour
        contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        holeCounter = 0
        for contour in contours:
            if (cv2.contourArea(contour) < 20000 and cv2.contourArea(contour) > 20):
                # draw out all the contour
                perimeter = cv2.arcLength(contour,True)
                vertices = cv2.approxPolyDP(contour, perimeter * 0.02, True)
                x, y, w, h = cv2.boundingRect(vertices)
                cv2.rectangle(self.img, (x,y),(x+w,y+h), (0,0,255),2)
            
                # Put text on top of the rectangle
                cv2.putText(self.img, 'Hole', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2, cv2.LINE_AA)
                holeCounter = holeCounter + 1

        # Put text to show number of hole detected
        cv2.putText(self.img, 'Hole detected: '+str(holeCounter), (0, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv2.LINE_AA)

        # show result
        cv2.imshow("result",self.img)
        cv2.waitKey(0)



