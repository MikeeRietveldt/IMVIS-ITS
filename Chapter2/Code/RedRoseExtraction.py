
# ITS IMVIS
# Chapter 2 - 
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 


img = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg') # LET OP OpenCV leest in BGR
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # foto van BGR naar HSV omzetten.
print(img.shape) # laat de array van de foto zien (640, 485)
print(img.dtype) # Laat het type zien van de foto, iedere entry is unit8
print(type(img)) # Laat zien wat de foto is (numpy.ndarray)

lr = np.array([0,120,70])   # low red
ur = np.array([15,255,255]) # upper red
mask1 = cv2.inRange(hsv,lr,ur)


print("Type mask: ", type(mask1))  # Laat zien wat dit mask is 
print("DType mask: ", mask1.dtype) # Laat het type van dit mask zien
print("Shape mask: ", mask1.shape) # Laat zien wat de array van dit mask is
print("Max value:", mask1.max(), "& Min value:", mask1.min()) # Laat de max en min value zien


lr = np.array([165,120,70])   # low red
ur = np.array([180,255,255]) # upper red
mask2 = cv2.inRange(hsv,lr,ur)

print("Mask1 unique: ", np.unique(mask1))
print("Mask2 unique: ", np.unique(mask2))

mask = mask1 | mask2 

res = cv2.bitwise_and(img, img, mask=mask)


plt.figure(1)    # Maakt een venster genaamd "1". Kan alles zijn
plt.subplot(121) # Verdeeld het figuur in (1 rij, 2 kolommen, 1e subplot actief.)
plt.imshow(img[:,:,::-1]) # Toon origineel (BGR -> RGB conversie)
plt.subplot(122) # Selecteert het volgende figuur (1e rij, 2e kolom, 2e subplot actief.)
plt.imshow(res[:,:,::-1]) # Toon origineel (BGR -> RGB conversie)
plt.show()