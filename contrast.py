import readwriteImg
import cv2
from PIL import Image, ImageEnhance

im = Image.open("./sample_images/landscape-mist-pine_trees.jpg")


def contrast(img, factor):
    enhancer = ImageEnhance.Contrast(img)
    im_output = enhancer.enhance(factor)
    im_output.save('./sample_images/contrast.jpg')

    return im_output


# Giam do tuong phan 0.5 lan
# contrast(im, 0.5)

# Tang do tuong phan len 1.5 lan
contrast(im, 1.5)

