
# ITS IMVIS
# Chapter 3 - 2x zoom
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 


colourImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg') # LET OP OpenCV leest in BGR


colourImage_resized = cv2.resize(src=colourImage, fx=2, fy=2, dsize=None) #fx = breedte -- fy = hoogte -- dsize = een zelf aan te geven hoogte (x, y) laat none als je mt fx,fy werkt





# Fotos laten zien in 1 venster.
plt.figure(1)    # Maakt een venster genaamd "1". Kan alles zijn
plt.subplot(121) # Verdeeld het figuur in (1 rij, 2 kolommen, 1e subplot actief.)
plt.imshow(colourImage[:,:,::-1]) # Toon origineel (BGR -> RGB conversie)
plt.subplot(122) # Selecteert het volgende figuur (1e rij, 2e kolom, 2e subplot actief.)
plt.imshow(colourImage_resized[:,:,::-1]) # Toon origineel (BGR -> RGB conversie)

plt.show() # laat alles zien
