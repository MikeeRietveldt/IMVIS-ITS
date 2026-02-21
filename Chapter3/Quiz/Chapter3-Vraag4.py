# ITS IMVIS
# Chapter 3 - Copy image and crop half + flip vertically
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 

grayImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Einstein1.jpg', cv2.IMREAD_GRAYSCALE) # LET OP OpenCV leest in BGR

numRows = grayImage.shape[0]
numCols = grayImage.shape[1] 

print(numRows, numCols)

grayImage_copy = np.zeros((int(numRows/2), numCols), dtype='uint8') # numrows / 2 om het zwarte weg te halen.

numRows = (int(numRows/2)) # int maken en dan delen door 2 om de foto te croppen.
# Loop om kopie te maken 
print(numRows)
for i in range(numRows): 
    for j in range(numCols):
            grayImage_copy[i,numCols-j-1] = grayImage[i,j] # kolom - j - 1 om foto te flippen

# Fotos laten zien in 1 venster.
plt.figure(1)    # Maakt een venster genaamd "1". Kan alles zijn
plt.subplot(121)
plt.imshow(grayImage, cmap='gray') # Toon origineel (BGR -> RGB conversie)
plt.subplot(122)
plt.imshow(grayImage_copy, cmap='gray') # Toon origineel (BGR -> RGB conversie)
plt.show() # Laat alles zien


