"""image_transform."""
import PIL
from PIL import Image
import numpy as np

class ImageTransform:
    """Image processing helper."""

    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)

    def scale(self, scale_size=256):
        """
        scale an image by resizing its shortest side to the given scale_size,
        and keeping its aspect ratio.
        """
        width, height = self.image.size
        resized_width = scale_size
        resized_height = scale_size
        if width >= height:
            height_percent = (scale_size / float(height))
            resized_width = int((float(width) * float(height_percent)))
        else:
            width_percent = (scale_size / float(width))
            resized_height = int((float(height) * float(width_percent)))

        img = self.image.resize((resized_width, resized_height), PIL.Image.ANTIALIAS)

        return img

    def center_crop(self, size=224):
        """
        crop an image from the center by the given size.
        """
        width, height = self.image.size
        (left, upper, right, lower) = (
            (width - size)/2,
            (height - size)/2,
            (width + size)/2,
            (height + size)/2
        )
        img = self.image.crop((left, upper, right, lower))

        return img

    def horizontal_flip(self):
        """
        horizontally flip an image.
        """
        img = self.image.transpose(PIL.Image.FLIP_TOP_BOTTOM)

        return img

    def normalize(self, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):
        """normalize an image"""
        mean = np.array(mean)
        std = np.array(std)
        img = np.array(self.image)

        img = img / 255
        img = (img - mean) / std
        img = Image.fromarray(img, 'RGB')

        return img
