# ITS IMVIS
# Chapter 2 - vraag 3 (rgb en bgr foto maken)
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 

# CIM == Colored Image
cim = plt.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg') # inladen met matplot, deze leest in RGB 

print(type(cim)) # laat de array van de foto zien (640, 485)
print(cim.dtype) # Laat het type zien van de foto, iedere entry is unit8
print(cim.shape) # Laat zien wat de foto is (numpy.ndarray)
print(cim) # laat de array van de image zien



cim = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg') # OpenCV leest in BGR

cim[:, 0:500, 0] = 255     # rood vlak links
cim[:, 500:1000, 1] = 255  # groen vlak midden
cim[:, 1000:1500, 2] = 255  # blauw vlak rechts

# plt om het in RGB te laten zien
plt.imshow(cim)
plt.show()

# Aanroepen van cv2, aangezien deze automatisch BGR doet.
cv2.imshow('BGR', cim)
cv2.waitKey(0)
cv2.destroyAllWindows()
