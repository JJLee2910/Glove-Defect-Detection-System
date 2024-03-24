import cv2
import numpy as np
from Detectors.base import Detector
from tools.resizer import Resizer

class DirtyPlasticGlovesDetector(Detector):
    def __init__(self, img) -> None:
        self.img = img

    def detect(self):
        # Convert the image to HSV color space for better color segmentation
        hsv_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds of the color range for white and beige-ish colors
        lower_white = np.array([0, 0, 180])  # Adjust these values based on your white color range
        upper_white = np.array([180, 50, 255])  # Adjust these values based on your white color range
        lower_beige = np.array([5, 50, 100])  # Adjust these values based on your beige-ish color range
        upper_beige = np.array([30, 150, 200])  # Adjust these values based on your beige-ish color range

        # Create masks to identify white and beige-ish colors separately
        white_mask = cv2.inRange(hsv_img, lower_white, upper_white)
        beige_mask = cv2.inRange(hsv_img, lower_beige, upper_beige)
        bg_mask = cv2.bitwise_or(white_mask, beige_mask)
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
        result_img = self.img.copy()
        for contour in contours:
            # Calculate the minimum enclosing circle for each contour
            ((x, y), radius) = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            # Draw the circle with a larger radius
            cv2.circle(result_img, center, radius + 10, (0, 0, 255), 5)  # Increase the radius by 10

        # Add text based on dots detection
        if len(contours) > 0:
            text = "Dirty gloves detected"
            text_color = (0, 0, 255)  # Red color for dirty gloves
        else:
            text = "Clean gloves detected"
            text_color = (0, 255, 0)  # Green color for clean gloves

        # Add text to the result image
        cv2.putText(result_img, text, (50, result_img.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 6, text_color, 7, cv2.LINE_AA)

        # Resize the result image
        result_img = Resizer.apply(result_img)

        # Display the result image with text and circles
        cv2.imshow("Gloves and Dots Detection Result", result_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
