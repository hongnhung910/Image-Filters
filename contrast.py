import readwriteImg
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import matplotlib.pyplot as plt 
#im = Image.open("./sample_images/landscape-mist-pine_trees.jpg")


def contrast(img, factor):
    enhancer = ImageEnhance.Contrast(img)
    im_output = enhancer.enhance(factor)
    return im_output


# Giam do tuong phan 0.5 lan
# contrast(im, 0.5)

# Tang do tuong phan len 1.5 lan
#contrast(im, 1.5)

def compute_hist(img): 

    hist = np.zeros((256,), np.uint8) 

    h, w = img.shape[:2] 

    for i in range(h): 

        for j in range(w): 

            hist[img[i][j]] += 1 

    return hist 

def equal_hist(hist): 

    cumulator = np.zeros_like(hist, np.float64) 

    for i in range(len(cumulator)): 

        cumulator[i] = hist[:i].sum() 

    print(cumulator) 

    new_hist = (cumulator - cumulator.min())/(cumulator.max() - cumulator.min()) * 255 

    new_hist = np.uint8(new_hist) 

    return new_hist 

# Ham tinh histogram
def compute_hist(img): 

    hist = np.zeros((256,), np.uint8) 

    h, w = img.shape[:2] 

    for i in range(h): 

        for j in range(w): 

            hist[img[i][j]] += 1 

    return hist 

# Ham can bang histogram
def equal_hist(hist): 

    cumulator = np.zeros_like(hist, np.float64) 

    for i in range(len(cumulator)): 

        cumulator[i] = hist[:i].sum() 

    print(cumulator) 

    new_hist = (cumulator - cumulator.min())/(cumulator.max() - cumulator.min()) * 255 

    new_hist = np.uint8(new_hist) 

    return new_hist 
