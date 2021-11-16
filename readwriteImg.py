import cv2
import os
def load_image(path, imgtype="color"):
    if imgtype=="color":
        return cv2.imread(path, cv2.IMREAD_COLOR)
    elif imgtype=="grayscale":
        return cv2.imread(path, cv2.IMREAD_GRAYSCALE)
def save_image(img, path):
    cv2.imwrite(path,img)
          
