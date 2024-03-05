import cv2

TARGET_HEIGHT = 500

class Resizer:
    @staticmethod
    def apply(image, th=TARGET_HEIGHT):

        img_height = image.shape[0]
        ratio = th / img_height

        return cv2.resize(image, None, fx=ratio, fy=ratio)