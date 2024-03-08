import cv2 as cv
import numpy as np
from Detectors.base import Detector

class TearingGloves(Detector):
    def __init__(self, img) -> None:
        self.img = img
        self.fixed_size = (500,500)
        self.frame = cv.resize(img, self.fixed_size, fx=0, fy=0, interpolation=cv.INTER_CUBIC)

    def detect(self):
        hsv_frame = cv.cvtColor(self.frame, cv.COLOR_BGR2HSV)
        # Mask for detecting glove
        lower = np.array([85, 111, 122])
        upper = np.array([103, 255, 255])
        mask = cv.inRange(hsv_frame, lower, upper)

        # apply median filtering
        blurred_frame = cv.medianBlur(mask, 9)

        # Define the structuring element (kernel) for erosion
        kernel = np.ones((3, 3), np.uint8)

        # Perform erosion
        eroded_frame = cv.erode(blurred_frame, kernel)

        # Find Contours
        contours, hierarchy = cv.findContours(mask.copy(), cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(eroded_frame, contours, -1, (0, 255, 0), 2)

        # Detect the defect within the glove
        internal_cnt = [contours[i] for i in range(len(contours)) if hierarchy[0][i][3] >= 0]

        if len(contours) > 0:
            blue_area = max(contours, key=cv.contourArea)
            (xg, yg, wg, hg) = cv.boundingRect(blue_area)

            # Draw rectangle for glove
            cv.rectangle(self.frame, (xg, yg), (xg + wg, yg + hg), (255, 0, 0), 1)

            # Label the glove
            self.frame = cv.putText(self.frame, 'Glove', (xg, yg - 5), cv.FONT_HERSHEY_SIMPLEX,
                                    0.5, (255, 0, 0), 1, cv.LINE_AA)

            # Find defect
            if len(internal_cnt) > 0:
                for i in internal_cnt:
                    # Check defect size
                    area = cv.contourArea(i)
                    print(area)
                    if area > 40:
                        xd, yd, wd, hd = cv.boundingRect(i)
                        # Draw rectangle for defect
                        cv.rectangle(self.frame, (xd, yd), (xd + wd, yd + hd), (0, 0, 255), 1)

                        # Label the defect
                        if area > 400:
                            # Defect Type: Tearing
                            self.frame = cv.putText(self.frame, 'Tearing', (xd, yd - 5), cv.FONT_HERSHEY_SIMPLEX,
                                                    0.5, (0, 0, 255), 1, cv.LINE_AA)
        cv.imshow('Result', self.frame)
        cv.waitKey(0)
        cv.destroyAllWindows()
