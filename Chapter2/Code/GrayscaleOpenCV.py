
# ITS IMVIS
# Chapter 2 - 
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 

img = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Pics\Einstein1.jpg', cv2.IMREAD_GRAYSCALE) # inladen van foto in openCV en in grayscale laden.

print(type(img)) # laat de array van de foto zien (640, 485)
print(img.dtype) # Laat het type zien van de foto, iedere entry is unit8
print(img.shape) # Laat zien wat de foto is (numpy.ndarray)
print(img) # laat de array van de image zien

img[23,100] = 200 # openCV geeft een geheel bewerkbare matrix, we hoeven dus geen kopie te maken zoals bij matplot.

cv2.imshow('Gray', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Ik vind het openen met matplotlib fijner aangezien ik daar de foto kan opslaan zoals hij is.
#hij opent daar ook in een apart venster.
#Ik kan daar de X en Y as zien met de cursor.