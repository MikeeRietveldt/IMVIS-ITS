
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





# Fotos laten zien in 1 venster.
plt.figure(1)    # Maakt een venster genaamd "1". Kan alles zijn
plt.subplot(141) # Verdeeld het figuur in (1 rij, 4 kolommen, 1e subplot actief.)
plt.imshow(colourImage[:,:,::-1]) # Toon origineel (BGR -> RGB conversie)
plt.subplot(142) # Selecteert het volgende figuur (1e rij, 2e kolom, 2e subplot actief.)
plt.imshow(grayImage, cmap='gray') # Toon origineel (BGR -> RGB conversie)
plt.subplot(143) # Selecteert het volgende figuur (1e rij, 3e kolom, 23e subplot actief.)
plt.imshow(grayImage_resized, cmap='gray') # Toon resized grayscale image
plt.subplot(144) # Selecteert het volgende figuur (1e rij, 4e kolom, 4e subplot actief.)
plt.imshow(colourImage_resized[:,:,::-1]) # Toon resized (BGR -> RGB conversie)
plt.show() # Laat alles zien
