# ITS IMVIS
# Chapter 2
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt

im = np.arange(256) # 256 rijen (breedte)
print(im.shape)

im = im[np.newaxis,:]
print(im.shape)

im = np.repeat(im,100,axis=0) # 100 kolommen (hoogte)
print(im.shape)
print(im)

plt.imshow(im, cmap='gray')
# plt.axis('off') # dit zet simpelweg de x en y as uit.
plt.show()
