import numpy as np
import matplotlib.pyplot as plt

im = np.arange(256)
print(im.shape)

im = im[np.newaxis,:]
print(im.shape)

im = np.repeat(im,100,axis=0)
print(im.shape)
print(im)

plt.imshow(im, cmap='gray')
plt.axis('off')
plt.show()
