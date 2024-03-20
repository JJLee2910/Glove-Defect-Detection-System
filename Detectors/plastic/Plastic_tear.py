import cv2
from tools.color_based_binarizer import ColorBasedBinarizer
from tools.resizer import Resizer

# Define the Detector class
class Detector:
    def __init__(self):
        pass

    def detect(self):
        pass

RESULT_IMG_TARGET_HEIGHT = 500
BLUE_LOWER_HUE = 90  # Adjust these values according to the blue color range
BLUE_HIGHER_HUE = 150  # Adjust these values according to the blue color range
BLUE_PIXEL_RATIO_OF_GLOVES = 50  # Adjust as needed

class Plastic_tear(Detector):
    def __init__(self, img) -> None:
        super().__init__()  # Call the constructor of the base class
        # Resize the input image to the target height
        self.img = Resizer.apply(img, RESULT_IMG_TARGET_HEIGHT)

    def detect(self):
        # Binarize the images based on color
        binarized_image = ColorBasedBinarizer.apply(self.img, 0.55, 1.0, 0.25)  # Adjust threshold parameters

        # Apply morphological operations to clean up the binary image
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        binarized_image = cv2.morphologyEx(binarized_image, cv2.MORPH_CLOSE, kernel)

        # Convert the resized binarized image to grayscale
        gray_image = cv2.cvtColor(binarized_image, cv2.COLOR_BGR2GRAY)

        # Detect contours in the grayscale image
        contours, _ = cv2.findContours(gray_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if not contours:
            result = self.tear_not_found(self.img)
            cv2.imshow("Result", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return

        # Iterate through each contour
        for contour in contours:
            # Calculate the number of blue pixels in the contour
            blue_pixel_num = 0
            for point in contour:
                x, y = point[0]
                hue_value = self.img[y, x, 0]  # Assuming hue is in the first channel

                # Check if the hue falls within the blue color range
                if BLUE_LOWER_HUE <= hue_value <= BLUE_HIGHER_HUE:
                    blue_pixel_num += 1

            # Calculate the blue pixel ratio
            ratio = blue_pixel_num / len(contour) * 100
            if ratio >= BLUE_PIXEL_RATIO_OF_GLOVES:
                # Draw a circle around the detected tear
                center, radius = cv2.minEnclosingCircle(contour)
                center = tuple(map(int, center))
                radius = int(radius)
                cv2.circle(self.img, center, radius, (0, 0, 255), 2)  # Red circle for tear
                result = self.tear_found(self.img)
                cv2.imshow("Result", result)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                return

        result = self.tear_not_found(self.img)
        cv2.imshow("Result", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def tear_found(self, img):
        cv2.putText(
            img,
            "Tear detected from blue gloves",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 0, 255),
            1,
            cv2.LINE_AA,
        )
        return img

    def tear_not_found(self, img):
        cv2.putText(
            img,
            "Tear not detected",
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )
        return img
