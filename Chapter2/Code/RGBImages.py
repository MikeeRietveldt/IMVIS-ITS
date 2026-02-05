# ITS IMVIS
# Chapter 2
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
cim = cim[:,:,::-1] #zorgt ervoor dat openCV weer RGB leest, dit is doormiddel van slicing met een negatieve stap. IPV [0,1,2] --> [2,1,0]

R = cim[:,:,0] # R[Rij, kolom, kanaal] 0 = rood
G = cim[:,:,1] # G[Rij, kolom, kanaal] 1 = groen
B = cim[:,:,2] # B[Rij, kolom, kanaal] 2 = blauw

R[100:400, 100:400] = 255
G[100:400, 100:400] = 0
B[100:400, 100:400] = 0
cim[:,:,0] = R
cim[:,:,1] = G
cim[:,:,2] = B

plt.figure(1)

plt.subplot(231) # (nrows(2), ncols(3), index(1))
plt.imshow(cim)
plt.axis('off') # zet simpelweg de x en y as
plt.subplot(232)
plt.imshow(cim)
plt.axis('off') # zet simpelweg de x en y as
plt.subplot(233)
plt.imshow(cim)
plt.axis('off') # zet simpelweg de x en y as

plt.subplot(234)
plt.imshow(R, cmap='gray') # laat de rode channel zien
plt.axis('off') # zet simpelweg de x en y as
plt.title('rood')
plt.subplot(235)
plt.imshow(G, cmap='gray') # laat de groene channel zien
plt.axis('off') # zet simpelweg de x en y as
plt.title('groen')
plt.subplot(236)
plt.imshow(B, cmap='gray') # laat de blauwe channel zien
plt.axis('off') # zet simpelweg de x en y as
plt.title('blauw')


plt.show()
