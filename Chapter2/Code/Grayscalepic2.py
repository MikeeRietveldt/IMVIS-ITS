
# ITS IMVIS
# Chapter 2
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt

im = plt.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Pics\Einstein1.jpg')
print(im.shape) # laat de array van de foto zien (640, 485)
print(im.dtype) # Laat het type zien van de foto, iedere entry is unit8
print(type(im)) # Laat zien wat de foto is (numpy.ndarray)
print(im) # laat de array van de image zien

plt.imshow(im, cmap='gray')
# plt.axis('off') # zet simpelweg de x en y as
plt.show()

print(im[23,300]) # Print de waarde van de pixel op 23,300 uit (23 hoogte, 300 breedte [hoogte, breedte])\
# print(im[23:100, 40:100]) # Print 24-99 && 41-99 
# de indexering is Y - X qua as.


im2 = im.copy() # kopie maken van im aangezien im read-only is.
im2[23:100, 40:100] = 255 #maak een geheel stuk wit.

plt.imshow(im2, cmap='gray') 
plt.show()

print('test')