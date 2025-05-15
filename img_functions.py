import streamlit as st
import numpy as np
from PIL import Image
import cv2
from scipy import ndimage


"""Warpaffine"""

def warpaffine(image):
    rows, cols, ch = image.shape
    pts1 = np.float32([[50,50],
                [200,50],
                [50,200]])
    pts2 = np.float32([[50,100],
                       [200,50],
                       [150,200]])
    
    points = cv2.getAffineTransform(pts1, pts2)
    img = cv2.warpAffine(image, points, (cols, rows))
    img_conv = Image.fromarray(img)
    return img_conv

"""Image Rotation"""

def img_rotation(image, *argv):
    rotated = ndimage.rotate(image, *argv)
    rot_img = Image.fromarray(rotated)
    return rot_img

"""Image Flipping"""

def img_flipping(image, *argv):
    flipped = cv2.flip(image, *argv)
    img_flipped = Image.fromarray(flipped)
    return img_flipped

    

