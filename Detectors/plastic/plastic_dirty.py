import cv2
import numpy as np  # Import NumPy
from tools.resizer import Resizer

# Define the Detector class
class Detector:
    def __init__(self):
        pass

    def detect(self):
        pass

RESULT_IMG_TARGET_HEIGHT = 500
DIRT_CONTOUR_AREA_THRESHOLD = 5000  # Adjust this threshold as needed

class DirtyPlasticGlovesDetector(Detector):
    def __init__(self, img) -> None:
        super().__init__()  # Call the constructor of the base class
        # Resize the input image to the target height
        self.img = Resizer.apply(img, RESULT_IMG_TARGET_HEIGHT)

    def detect(self):
        # Convert the resized image to grayscale
        gray_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to create a binary image
        _, binary_image = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY_INV)

        # Apply morphological operations to clean up the binary image
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        morph_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

        # Find contours in the morphological image
        contours, _ = cv2.findContours(morph_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            result = self.no_dirt_detected(self.img)
            cv2.imshow("Result", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return

        # Segment and analyze each contour
        for contour in contours:
            # Create a mask for the contour
            mask = np.zeros_like(gray_image)
            cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)

            # Extract the segmented region
            segmented_region = cv2.bitwise_and(gray_image, gray_image, mask=mask)

            # Calculate the area of the segmented region
            area = cv2.contourArea(contour)

            # Detect dirt based on the area threshold
            if area >= DIRT_CONTOUR_AREA_THRESHOLD:
                # Draw a contour around the detected area
                cv2.drawContours(self.img, [contour], -1, (0, 255, 0), 2)  # Green contour for detected area
                result = self.dirt_detected(self.img)
                cv2.imshow("Result", result)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                return

        result = self.no_dirt_detected(self.img)
        cv2.imshow("Result", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def dirt_detected(self, img):
        cv2.putText(
            img,
            "Dirty plastic gloves detected",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            1,
            cv2.LINE_AA,
        )
        return img

    def no_dirt_detected(self, img):
        cv2.putText(
            img,
            "No dirt detected on plastic gloves",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )
        return img

