import cv2
import numpy as np
from Detectors.base import Detector
from tools.color_based_binarizer import ColorBasedBinarizer
from tools.resizer import Resizer

class markedfinger(Detector):
    def __init__(self, img) -> None:
        self.img = img

    def detect(self):
        # Convert the image to HSV color space for better color segmentation
        hsv_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds of the color range for beige background
        lower_beige = np.array([5, 20, 70])  # Adjust these values based on your background color
        upper_beige = np.array([30, 255, 255])  # Adjust these values based on your background color

        # Create a mask to identify the beige background pixels
        bg_mask = cv2.inRange(hsv_img, lower_beige, upper_beige)

        # Invert the mask to get a mask for the gloves
        fg_mask = cv2.bitwise_not(bg_mask)

        # Apply the foreground mask to extract the gloves
        gloves_img = cv2.bitwise_and(self.img, self.img, mask=fg_mask)

        # Convert the gloves image to grayscale
        grey = cv2.cvtColor(gloves_img, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise and enhance dot detection
        blurred = cv2.GaussianBlur(grey, (11, 11), 0)

        # Threshold the blurred image to create a binary mask for black dots
        _, thresh = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY_INV)

        # Find contours in the binary image
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw circles around the detected black dots on the gloves image
        result_img = gloves_img.copy()
        cv2.drawContours(result_img, contours, -1, (0, 0, 255), 2)

        # Add text based on dots detection
        if len(contours) > 0:
            cv2.putText(result_img, "Dots detected", (70, result_img.shape[0] - 70), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 255), 20)
        else:
            cv2.putText(result_img, "Dots not detected", (100, result_img.shape[0] - 70), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 255, 0), 20)

        # Resize the result image
        result_img = Resizer.apply(result_img)

        # Display the result image with black dots highlighted and text
        cv2.imshow("Black Dots Detection Result", result_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
