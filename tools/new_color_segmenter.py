import numpy as np
from skimage.color import rgb2hsv

class ColorBasedSegmenter:
    @staticmethod  
    def apply(img, lower_hue, upper_hue, saturation_threshold):
        hsv_image = rgb2hsv(img)

        lower_mask = hsv_image[..., 0] > lower_hue
        upper_mask = hsv_image[..., 0] < upper_hue
        saturation_mask = hsv_image[..., 1] > saturation_threshold

        mask = np.logical_and.reduce((lower_mask, upper_mask, saturation_mask))
        masked_image = img * np.expand_dims(mask, axis=2)

        return masked_image