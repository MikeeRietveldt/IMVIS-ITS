# ITS IMVIS
# Chapter 6 - 
# Mike Rietveldt - 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib as mpl


grayImage = plt.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Einstein1.jpg') 
BinaryImage = plt.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Binary.png')  


K_rect = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)) # k is kernal (numpy ndarray)
K_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
K_cross = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

print('Rectangle \n', K_rect)
print('Ellipse \n', K_ellipse)
print('cross \n', K_cross)