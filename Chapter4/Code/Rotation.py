# ITS IMVIS
# Chapter 4 - 
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




# -------------------------------------------------------------------------- Chapter 4 dingen.

a = 45 # angle
ca = np.cos(np.deg2rad(a))
sa = np.cos(np.deg2rad(a))
R = np.array([[ca,-sa],[sa,ca]]) # definieren van matrix

rMax = grayImage.shape[0] # maximale rows
cMax = grayImage.shape[1] # maximale columns
Cords = np.array([[0,0],[0,cMax-1],[rMax-1,0],[rMax-1,cMax-1]]) # coordinaten
A_dash = R.dot(Cords.T) 
mins = A_dash.min(axis=1)
maxs = A_dash.max(axis=1) 
minR = np.int64(np.floor(mins[0])) # minimale aantal rows
minC = np.int64(np.floor(mins[1])) # minimale aantal columns
maxR = np.int64(np.ceil(maxs[0])) # maximale aantal rows
maxC = np.int64(np.ceil(maxs[1])) # maximale aantal columns
H = maxR - minR + 1 # Hoogte
W = maxC - minC + 1 # Breedte
I2 = np.zeros((H,W), dtype='uint8') # image result in I2 opslaan

print(R)
print(Cords.shape)
print(A_dash)
print(mins)
print(maxs)
print(I2.shape)


Tinv = np.linalg.inv(R) # Inverse R
for new_i in range(minR, maxR):
     for new_j in range(minC, maxC):
                P_dash = np.array([new_i,new_j])
                P = Tinv.dot(P_dash)
                i = P[0]
                j = P[1]
                #bump check
                if i < 0 or i >= numRows or j< 0 or j >= numCols:
                    pass
                else:  
                    g = f_bilinearInterpolate(i,j,grayImage)
                    I2[new_i-minR,new_j-minC] = g


# functies aanroepen
    #grayscale
displayImageInActualSize(I2)

