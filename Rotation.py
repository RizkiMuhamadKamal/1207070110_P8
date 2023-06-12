#import library
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#memanggil gambar
img = cv.imread('Rizki.jpg')
h,w = img.shape[:2]

rotation_matrix = cv.getRotationMatrix2D((w/2,h/2), -180, 0.5)
rotated_img = cv.warpAffine(img, rotation_matrix, (w, h))

plt.imshow(cv.cvtColor(rotated_img, cv.COLOR_BGR2RGB))
plt.title("Rotation")
plt.show()