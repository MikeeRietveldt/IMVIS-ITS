# ITS IMVIS
# Chapter 6 - 
# Mike Rietveldt - 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib as mpl


grayImage = plt.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Einstein1.jpg') 
BinaryImage = plt.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Binary.png')  

plt.imshow(BinaryImage)
plt.show()
print('binaire foto', np.unique(BinaryImage)) # alleen 0 en 1 vanwege binary.

plt.imshow(grayImage, cmap='gray')
plt.show()
print('grijze foto', np.unique(grayImage))

th = 150
im2 = grayImage>th

plt.imshow(~(im2), cmap='gray')
plt.show()
print('grijze foto na threshhold', np.unique(im2))