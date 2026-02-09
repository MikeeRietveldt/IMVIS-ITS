
# ITS IMVIS
# Chapter 2 - 
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 

def f_rgb_to_hsv(r, g, b, scaleFactor): 
    r = r / 255.0 # normaliseren r
    g = g / 255.0 # normaliseren g
    b = b / 255.0 # normaliseren b
    cmax = max(r, g, b)   # max van r, g, b
    cmin = min(r, g, b)   # min r, g, b
    diff = cmax - cmin    # verschil van cmax en cmin.

    if cmax == cmin:
        h = 0
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 0) % 360
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    if h < 0:
        h = h + 360

    # Saturatie berekenen
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * scaleFactor

    # Value berekenen
    v = cmax * scaleFactor

    return h, s, v

# print buiten de functie om resultaten te zien
print(f_rgb_to_hsv(100, 200, 50, 100)) # vul hier waardes in - r, g, b, scaleFactor


im = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg') # LET OP OpenCV leest in BGR
HsvIm = cv2.cvtColor(im, cv2.COLOR_BGR2HSV) 
print(im.shape) # laat de array van de foto zien (640, 485)
print(im.dtype) # Laat het type zien van de foto, iedere entry is unit8
print(type(im)) # Laat zien wat de foto is (numpy.ndarray)