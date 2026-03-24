# ITS IMVIS
# Chapter 5 - 
# Mike Rietveldt - 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib as mpl


grayImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Einstein1.jpg',cv2.IMREAD_GRAYSCALE)  # LET OP OpenCV leest in BGR
colourImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\Rgb1.jpg')  # LET OP OpenCV leest in BGR
AffineWarpedImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\EinsteinWarped.png',cv2.IMREAD_GRAYSCALE)  
ProjectiveWarpedImage = cv2.imread(r'C:\Users\Mike\Desktop\ITS\Imvis\Chatpter2\Pics\EinsteinProjective.png',cv2.IMREAD_GRAYSCALE)  

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


def f_getExtentsProjective(T, rMax, cMax):
    Cords = np.array([[0,0,1],[0,cMax-1,1],[rMax-1,0,1],[rMax-1,cMax-1,1]]) # homogenius coordinaten
    print(Cords.shape) # kijken wat de array nu is
    A_dash = T.dot(Cords.T) 
    A_dash = A_dash/A_dash[2,:]
    mins = A_dash.min(axis=1)
    maxs = A_dash.max(axis=1) 
    minR = np.int64(np.floor(mins[0])) # minimale aantal rows
    minC = np.int64(np.floor(mins[1])) # minimale aantal columns
    maxR = np.int64(np.ceil(maxs[0])) # maximale aantal rows
    maxC = np.int64(np.ceil(maxs[1])) # maximale aantal columns
    H = maxR - minR + 1 # Hoogte
    W = maxC - minC + 1 # Breedte    
    return minR, minC, maxR, maxC, H, W

def f_transformProjective(T, grayImage):
    rMax = grayImage.shape[0]
    cMax = grayImage.shape[1]
    minR, minC, maxR, maxC, H, W = f_getExtentsProjective(T, rMax, cMax)
    I2 = np.zeros((H,W), dtype='uint8')
    Tinv = np.linalg.inv(T) # Omzetten nar T
    for new_i in range(minR, maxR):
        for new_j in range(minC, maxC):
                P_dash = np.array([new_i,new_j,1]) # homogenius
                P = Tinv.dot(P_dash)
                P = P/P[2]
                i = P[0]
                j = P[1]
                #bump check
                if i < 0 or i >= numRows or j< 0 or j >= numCols:
                    pass
                else:  
                    g = f_bilinearInterpolate(i,j,grayImage)
                    I2[new_i-minR,new_j-minC] = g
    return I2

def f_getPoints(I, numPts):
    fig, ax = plt.subplots(1, figsize=(15,30))
    plt.imshow(I, cmap='gray')
    pts = np.round(np.array(plt.ginput(n=numPts)))
    pts = pts[:,[1,0]].T
    plt.close()
    return pts

#pts = f_getPoints(grayImage, 4) # aangeven hoeveel punten je wilt aanklikken in de foto.
P = f_getPoints(grayImage, 5)
P_dash = f_getPoints(AffineWarpedImage, 5)

P = np.vstack((P,np.ones((1,5))))
P_dash = np.vstack((P_dash,np.ones((1,5))))
A = P_dash.dot(P.T).dot(np.linalg.inv(P.dot(P.T)))
print(A) 

#print(pts)
print(P)
print(P_dash)

I2 = f_transformProjective(A, grayImage)
plt.figure(1)
plt.subplot(121)
plt.imshow(I2, cmap='gray')
plt.subplot(122)
plt.imshow(AffineWarpedImage, cmap='gray')
plt.show()