
# ITS IMVIS
# Chapter 2 - YellowRoseExtraction
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 


img = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg') # LET OP OpenCV leest in BGR
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # foto van BGR naar HSV omzetten.
print(img.shape) # laat de array van de foto zien (640, 485)
print(img.dtype) # Laat het type zien van de foto, iedere entry is unit8
print(type(img)) # Laat zien wat de foto is (numpy.ndarray)

ly = np.array([20,100,100]) # Lower yellow
uy = np.array([35,255,255]) # Upper yellow
mask = cv2.inRange(hsv,ly,uy)


res = cv2.bitwise_and(img, img, mask=mask)


plt.figure(1)    # Maakt een venster genaamd "1". Kan alles zijn
plt.subplot(121) # Verdeeld het figuur in (1 rij, 2 kolommen, 1e subplot actief.)
plt.imshow(img[:,:,::-1]) # Toon origineel (BGR -> RGB conversie)
plt.subplot(122) # Selecteert het volgende figuur (1e rij, 2e kolom, 2e subplot actief.)
plt.imshow(res[:,:,::-1]) # Toon origineel (BGR -> RGB conversie)
plt.show()