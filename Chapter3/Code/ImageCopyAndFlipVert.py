# ITS IMVIS
# Chapter 3 - 
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 


colourImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg') # LET OP OpenCV leest in BGR
grayImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Einstein1.jpg', cv2.IMREAD_GRAYSCALE) # LET OP OpenCV leest in BGR



numRows = grayImage.shape[0]
numCols = grayImage.shape[1] 

print(numRows, numCols)

grayImage_copy = np.zeros((numRows, numCols), dtype='uint8')

# Loop om kopie te maken
for i in range(numRows): 
    for j in range(numCols):
            grayImage_copy[i,j] = grayImage[i,j]

# Fotos laten zien in 1 venster.
plt.figure(1)    # Maakt een venster genaamd "1". Kan alles zijn
plt.subplot(121)
plt.imshow(grayImage, cmap='gray') # Toon origineel (BGR -> RGB conversie)
plt.subplot(122)
plt.imshow(grayImage_copy, cmap='gray') # Toon origineel (BGR -> RGB conversie)
plt.show() # Laat alles zien


