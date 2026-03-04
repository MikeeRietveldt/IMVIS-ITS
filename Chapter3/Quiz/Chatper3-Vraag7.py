# ITS IMVIS
# Chapter 3 - Exam 1 + Exam 2
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 
import matplotlib as mpl

def f_bilinearInterpolate(r,c,I):
    lc = int(c) # int maken van de waarde
    rc = lc + 1 # linker kolom + 1 = rechter kolom
    wr = c - lc # kolom - linker kolom = breedte rechts
    wl = rc - c # rechter kolom - kolom = breedte links
    tr = int(r) # int maken van de warde
    br = tr + 1 # bovenste rij + 1 = achterste rij
    wt = br - r # achterste rij - rij = breedte boven
    wb = r - tr # rij + bovenste rij = breedte beneden
    if tr >= 0 and br< I.shape[0] and lc >= 0 and rc < I.shape[1]:
        a = wl*I[tr,lc] + wr*I[tr,rc]
        b = wl*I[br,lc] + wr*I[br,rc]
        g = wt*a + wb*b
        return np.uint8(g)
    else:
         return 0



grayImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Einstein1.jpg', cv2.IMREAD_GRAYSCALE) # LET OP OpenCV leest in BGR
colourImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg') # LET OP OpenCV leest in BGR

numRows = grayImage.shape[0]
numCols = grayImage.shape[1] 

# scale matrix maken
def scale_matrix(scale):
    size = len(scale)
    matrix = np.zeros((size,size))
    for i,_ in enumerate(matrix):
         matrix[i][i] = scale[i]
    return matrix

# image scalen
def f_scaleImage(scale, grayImage):
    numRows = grayImage.shape[0]
    numCols = grayImage.shape[1]
    S = scale_matrix(scale)
    print(S) # uitkomst checken
    I2 = np.zeros((int(scale[0])*numRows, int(scale[1])*numCols), dtype='uint8')
    Tinv = np.linalg.inv(S) # inverse lineare algebra
    for new_i in range(I2.shape[0]): 
        for new_j in range(I2.shape[1]):
                P_dash = np.array([new_i,new_j])
                P = Tinv.dot(P_dash)
                # P = np.int16(np.round(P)) # floor rond af naar beneden
                i = P[0]
                j = P[1]
                #bump check
                if i < 0 or i >= numRows or j< 0 or j >= numCols:
                    pass
                else:  
                    g = f_bilinearInterpolate(i,j,grayImage)
                    I2[new_i,new_j] = g
    return I2



# Functie voor laten zien originele foto grayscale
def displayImageInActualSize(I):
      dpi = mpl.rcParams['figure.dpi'] # Intensiteit
      H,W = I.shape # Hoogte, breedte
      figSize = W/float(dpi), H/float(dpi) # Hoogte, breedte delen door intensiteit
      fig = plt.figure(figsize = figSize) # Grootes gelijk stellen van figguur aan foto
      ax = fig.add_axes([0,0,1,1]) # Axes aanmaken
      #ax.axis('off')
      ax.imshow(I, cmap='gray')
      plt.show()



# Functie voor laten zien originele foto kleur
def displayImageInActualSizeColor(I):
      dpi = mpl.rcParams['figure.dpi'] # Intensiteit
      H,W = I.shape[0:2] # Hoogte, breedte en de kleurenkanalen
      figSize = W/float(dpi), H/float(dpi) # Hoogte, breedte delen door intensiteit
      fig = plt.figure(figsize = figSize) # Grootes gelijk stellen van figguur aan foto
      ax = fig.add_axes([0,0,1,1]) # Axes aanmaken
      #ax.axis('off')
      ax.imshow(I)
      plt.show()    


I_color = colourImage[:,:,::-1]
scale = [2,2]
r = f_scaleImage(scale,I_color[:,:,0]) # rood
g = f_scaleImage(scale,I_color[:,:,1]) # groen
b = f_scaleImage(scale,I_color[:,:,2]) # blauw

C = np.zeros((r.shape[0], r.shape[1],3), dtype=np.uint8)
C[:,:,0] = r
C[:,:,1] = g
C[:,:,2] = b



# functies aanroepen
    #grayscale
scaled = f_scaleImage([2,2], grayImage) # test hier
displayImageInActualSize(scaled)

    #kleur
displayImageInActualSizeColor(I_color)
#displayImageInActualSizeColor(C)

