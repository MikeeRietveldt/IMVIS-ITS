# ITS IMVIS
# Chapter 4 - vraag 3 (openCV rotatie)
# Mike Rietveldt - 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib as mpl


grayImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Einstein1.jpg',cv2.IMREAD_GRAYSCALE)  # LET OP OpenCV leest in BGR

colourImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg')  # LET OP OpenCV leest in BGR

numRows = grayImage.shape[0]
numCols = grayImage.shape[1]


# Functie voor laten zien originele foto grayscale
def displayImageInActualSize(I):
    dpi = mpl.rcParams['figure.dpi']  # Intensiteit
    H, W = I.shape  # Hoogte, breedte
    figSize = W / float(dpi), H / float(dpi)  # Hoogte, breedte delen door intensiteit
    fig = plt.figure(figsize=figSize)  # Grootes gelijk stellen van figguur aan foto
    ax = fig.add_axes([0, 0, 1, 1])  # Axes aanmaken
    # ax.axis('off')
    ax.imshow(I, cmap='gray')
    plt.show()


# -------------------------------------------------------------------------- Chapter 4 dingen.

# Oplossing quiz 

image = grayImage
image_center = tuple(np.array(image.shape[1::-1]) / 2)
a = 90  # angle
scale = 1.0
T = cv2.getRotationMatrix2D(image_center, a, scale) # kan image_center ook aanpassen met bijvoorbeeld (0,0)
print(T)
print(image.shape)
print(image_center)
I2 = cv2.warpAffine(image, T, image.shape[1::-1])



# functies aanroepen
# grayscale
displayImageInActualSize(I2)