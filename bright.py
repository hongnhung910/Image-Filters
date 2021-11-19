import readwriteImg
import cv2
from PIL import Image, ImageEnhance

image = cv2.imread('./sample_images/landscape-mist-pine_trees.jpg')
im = Image.open("./sample_images/landscape-mist-pine_trees.jpg")

# Version Official: Quite fast(acceptable) + based on Lecture Theory
def brightAdjust(img, change):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)
    for i in range(0, len(v)):
        for j in range(0, len(v[0])):
            test = v[i][j] + change
            if test > 255:
                v[i][j] = 255
            elif test < 0:
                v[i][j] = 0
            else:
                v[i][j] += change

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    readwriteImg.save_image(img, './sample_images/brightAdjust.jpg')

    return img

# Version 1: Chua kiem chung lai - Very fast
def brightAdjust1(img, change):
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - change
    v[v > lim] = 255
    v[v <= lim] += change

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    readwriteImg.save_image(img, './sample_images/brightAdjust1.jpg')

    return img

# Version 2: Su dung them lib: PIL
def brightAdjust2(img, factor):
    enhancer = ImageEnhance.Brightness(img)
    im_output = enhancer.enhance(factor)
    im_output.save('./sample_images/brightAdjust2.jpg')

    return  im_output

brightAdjust(image,-100)
# brightAdjust1(image,100)
# brightAdjust2(im,2)