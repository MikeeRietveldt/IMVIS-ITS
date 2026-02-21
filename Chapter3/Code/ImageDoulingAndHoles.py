# ITS IMVIS
# Chapter 3 - 
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 
import matplotlib as mpl

grayImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Einstein1.jpg', cv2.IMREAD_GRAYSCALE) # LET OP OpenCV leest in BGR

numRows = grayImage.shape[0]
numCols = grayImage.shape[1] 


S = np.array([[2, 0],[0, 2]]) # array aanmaken 
I2 = np.zeros((2*numRows, 2*numCols), dtype='uint8')

# Loop om kopie te maken
for i in range(numRows): 
    for j in range(numCols):
            P = np.array([i,j])
            P_dash = S.dot(P)
            new_i = P_dash[0]
            new_j = P_dash[1]
            I2[new_i,new_j] = grayImage[i,j]

print(grayImage.shape)
print(I2.shape)

# Functie voor laten zien originele foto
def displayImageInActualSize(I):
      dpi = mpl.rcParams['figure.dpi'] # Intensiteit
      H,W = I.shape # Hoogte, breedte
      figSize = W/float(dpi), H/float(dpi) # Hoogte, breedte delen door intensiteit
      fig = plt.figure(figsize = figSize) # Grootes gelijk stellen van figguur aan foto
      ax = fig.add_axes([0,0,1,1]) # Axes aanmaken
      #ax.axis('off')
      ax.imshow(I, cmap='gray')
      plt.show()

displayImageInActualSize(I2)
