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

E_rect = cv2.erode(BinaryImage, K_rect)
E_ellipse = cv2.erode(BinaryImage, K_ellipse)
E_cross = cv2.erode(BinaryImage, K_cross)
plt.subplot(221)
plt.imshow(BinaryImage)
plt.title('Origineel')
plt.subplot(222)
plt.imshow(E_rect)
plt.title('Rect')
plt.subplot(223)
plt.imshow(E_ellipse)
plt.title('Ellipse')
plt.subplot(224)
plt.imshow(E_cross)
plt.title('Cross')
plt.show()

print('Rect - ellipse \n',np.sum((E_rect - E_ellipse)**2))
print('Rect - cross \n',np.sum((E_rect - E_cross)**2))