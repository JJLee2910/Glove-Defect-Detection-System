import cv2
import numpy as np

class ColorBasedBinarizer:
    @staticmethod
    def apply(img_bgr, color_ranges):
        # Convert the image from BGR to RGB (OpenCV loads images in BGR format)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

        # Convert the image to HSV
        img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

        # Combine the masks
        mask = cv2.inRange(img_hsv, color_ranges[0][0], color_ranges[0][1])
        for i in range(1, len(color_ranges)):
            lower_bound = color_ranges[i][0]
            upper_bound = color_ranges[i][1]
            new_mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
            mask = cv2.bitwise_or(mask, new_mask)

        # Create a black image
        result = np.zeros_like(img_rgb)

        # Set pixels within the pink color range to white in the result image
        result[mask != 0] = [255, 255, 255]

        return result

# test code
# img = cv2.imread("./Images/Silicone/missing_finger_1.jpeg")

# # Define the pink color range in HSV
# lower_pink = np.array([120, 20, 145])
# upper_pink = np.array([180, 255, 255])

# lower_brown = np.array([0, 20, 145])
# upper_brown = np.array([20, 255, 255])

# ranges = [
#     [lower_pink, upper_pink],
#     [lower_brown, upper_brown]
# ]

# # how this class is used
# result = ColorBasedBinarizer.apply(img, ranges)

# # morphological operation - opening for denoising
# kernel = np.ones((5, 5), np.uint8) 
# result=cv2.dilate(result, kernel, iterations=1)
# result=cv2.erode(result, kernel, iterations=3)

# cv2.imshow("orig", img)
# cv2.imshow("res", result)
# cv2.waitKey(0)