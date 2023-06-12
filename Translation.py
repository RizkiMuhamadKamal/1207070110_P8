#import library
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#memanggil gambar
img = cv.imread('Rizki.jpg')
h,w = img.shape[:2]

half_height, half_width = h//4, w//8
transition_matrix = np.float32([[1, 0, half_width], [0, 1, half_height]])
img_transition = cv.warpAffine(img, transition_matrix, (w, h))

plt.imshow(cv.cvtColor(img_transition, cv.COLOR_BGR2RGB))
plt.title('Translation')
plt.show()