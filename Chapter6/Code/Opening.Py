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

im_bool = np.array(BinaryImage[:,:,0],dtype = np.bool)
plt.imshow(im_bool, cmap='gray')
plt.show()

N = np.random.rand(im_bool.shape[0], im_bool.shape[1])
N_binary = N>0.98
plt.imshow(N_binary, cmap='gray')
plt.show()

img_N = im_bool | N_binary
plt.imshow(img_N, cmap='gray')
plt.show()

O_rect = cv2.morphologyEx(np.float32(img_N),cv2.MORPH_OPEN,K_rect)
plt.imshow(O_rect, cmap='gray')
plt.show()

E_rect = cv2.erode(np.float32(img_N),K_rect)
O_rect2 = cv2.dilate(E_rect,K_rect)
plt.imshow(O_rect2, cmap='gray')
plt.show()