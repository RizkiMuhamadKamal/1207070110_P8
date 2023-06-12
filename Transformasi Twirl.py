#import library
import cv2 as cv
import matplotlib.pyplot as plt
from skimage.transform import swirl

#memanggil gambar
img = cv.imread('Rizki.jpg')
#menerapkan efek swirl pada gambar
swirled = swirl(img, rotation=0, strength=15, radius=600)

#membuat figure (1 baris dan 2 kolom)
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3), sharex=True, sharey=True)

#menampilkan gambar asli
ax0.imshow(img[..., ::-1])#digunakan untuk mengubah urutan warna BGR to RGB
ax0.set_title('Original')
ax0.axis('off')

#menampilkan gambar efek swirl
ax1.imshow(swirled[..., ::-1])#digunakan untuk mengubah urutan warna BGR to RGB
ax1.set_title('Swirled')
ax1.axis('off')

#menampilkan output
plt.show()
