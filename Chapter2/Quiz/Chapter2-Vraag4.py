
# ITS IMVIS
# Chapter 2 - Vraag 4 (python command to convert HSV to RGB && BRG using open cv2)
# Mike Rietveldt -- 20183380

import numpy as np
import matplotlib.pyplot as plt
import cv2 

# aanmaken hsv pixel zodat je kunt aantonen of de conversie werkt.
hsv_pixel = np.array([[[0, 255, 255]]],dtype=np.uint8) # [H[B[k,k,k]]] 3 lagen, (hoogte (buitenste(1 pixel - h)), breedte (middelste(1 pixel - b)), binnenste(3 kleuren - k)


BGRim = cv2.cvtColor(hsv_pixel, cv2.COLOR_HSV2BGR) # conversie HSV -> BGR 
RGBim = cv2.cvtColor(hsv_pixel, cv2.COLOR_HSV2RGB) # conversie HSV -> RGB

print("HSV:", hsv_pixel[0, 0]) # verwachte uitkomst 0, 255, 255
print("BGR:", BGRim[0, 0]) # verwachte uitkomst 0, 0, 255
print("RGB:", RGBim[0, 0]) # verwachte uitkomst 255, 0, 0