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
N_binary = N<0.98
plt.imshow(N_binary, cmap='gray')
plt.show()

img_H = im_bool & N_binary
plt.imshow(img_H, cmap='gray')
plt.show()

C_rect = cv2.morphologyEx(np.float32(img_H),cv2.MORPH_CLOSE,K_rect)
plt.imshow(C_rect, cmap='gray')
plt.show()

D_rect = cv2.dilate(np.float32(img_H),K_rect)
C_rect2 = cv2.erode(D_rect,K_rect)
plt.imshow(C_rect2, cmap='gray')
plt.show()