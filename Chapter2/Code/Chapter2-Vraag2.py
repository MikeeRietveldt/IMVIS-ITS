
# ITS IMVIS
# Chapter 2 - vraag 2 (witte blokjes op ogen van Einstein.)
# Open de foto eerst normaal, plaats je muis op het oog en schrijf deze waardes op, vergeet niet x,y is omgedraaid in de array. Je moet dus y,x doen.
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt

im = plt.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Pics\Einstein1.jpg')

im2 = im.copy() # kopie maken van im aangezien im read-only is.
im2[200:240, 215:255] = 255 #maak rechteroog wit.
im2[210:235, 280:320] = 255 #maak linkeroog wit.

plt.imshow(im2, cmap='gray') 
plt.show()

print('test2')