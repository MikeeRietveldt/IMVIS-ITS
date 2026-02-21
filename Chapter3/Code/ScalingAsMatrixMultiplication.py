# ITS IMVIS
# Chapter 3 - 
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 


colourImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg') # LET OP OpenCV leest in BGR
grayImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Einstein1.jpg', cv2.IMREAD_GRAYSCALE) # LET OP OpenCV leest in BGR



grayImage_resized = cv2.resize(src=grayImage, fx=1.5, fy=0.8, dsize=None) #fx = breedte -- fy = hoogte -- dsize = een zelf aan te geven hoogte (x, y), laat none als je mt fx,fy werkt
colourImage_resized = cv2.resize(src=colourImage, fx=0.5, fy=2, dsize=None) #fx = breedte -- fy = hoogte -- dsize = een zelf aan te geven hoogte (x, y) laat none als je mt fx,fy werkt


P = np.array([2,4]) # Vermenigvuldigingen
Sx, Sy = 2,2 # Variabelen
S = np.array([[Sx, 0],[0, Sy]]) # array aanmaken 

P_dash = S.dot(P) # Matrix vermenigvuldiging

print(S)
print(P_dash)
