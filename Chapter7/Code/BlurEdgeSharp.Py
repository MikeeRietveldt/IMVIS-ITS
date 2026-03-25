import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy import signal


im = plt.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Bird.jpg')[:,:,:3]
imGray = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

smoothingMask = np.ones((15,15))/225
imBlurred = signal.convolve2d(imGray, smoothingMask, boundary='symm', mode='same')

plt.subplot(121)
plt.imshow(imGray, cmap='gray')
plt.title('Gray')
plt.subplot(122)
plt.imshow(imBlurred, cmap='gray')
plt.title('Blur')
plt.show()

xMask = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
yMask = xMask.T.copy()

fx = signal.convolve2d(imGray,xMask,boundary='symm',mode='same')
fy = signal.convolve2d(imGray,yMask,boundary='symm',mode='same')

print('f en y waarde:', fx.shape)
print('imgray waarde:',imGray.shape)

Gm = (fx**2 + fy**2)**0.5 # matrix
plt.imshow(Gm,cmap='gray')
plt.title('Edging')
plt.show()

th = Gm.max()-4*Gm.std() #threshhold
print('Threshhold waarde:', th)

E = Gm>th
plt.imshow(Gm>1,cmap='gray')
plt.title('threshhold')
plt.show()

imSharped = imBlurred + 5*Gm
plt.subplot(121)
plt.imshow(imBlurred, cmap='gray')
plt.title('Blurred')
plt.subplot(122)
plt.imshow(imSharped, cmap='gray')
plt.title('Sharp')
plt.show()