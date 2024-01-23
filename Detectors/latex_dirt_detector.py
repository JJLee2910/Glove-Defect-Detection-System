import cv2
import numpy as np
from tools.FindLatex import findLatexContour, findDirtColor


class DirtDetector:
    def __init__(self, img) -> None:
        self.img = img

    def detect(self):
        # Find the mask of the latex
        latexContour = findLatexContour(self.img)

        overlay = np.zeros((self.img.shape[0], self.img.shape[1],4),
                           dtype="uint8")
        
        if latexContour is None:
            return overlay
        
        # find the stain mask
        dirt_contour = findDirtColor(self.img)

        # find the min area of the rectangle
        
