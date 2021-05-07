import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# open an image from hard-drive 
img_name = "image.jpg"
img = cv.imread(img_name)
plt.imshow(img)
plt.show()

# split ultrawide image to diff pictures to test stitching
img1 = img[:, :1000]
img2 = img[:, 800:2000]
img3 = img[:, 1800:3000]
img4 = img[:, 2800:4000]
img5 = img[:, 3800:]

all_imgs = [img1, img2, img3, img4, img5]
for i in all_imgs:
  plt.imshow(i)
  plt.show()

  
# PANORAMA :: Mode for creating photo panoramas. (perspective transformation)
# SCANS    :: Mode for composing scans.          (affine transformation)
mode = cv.Stitcher_PANORAMA
m_stitcher = cv.Stitcher.create(mode)
status, pano = m_stitcher.stitch(all_imgs)
cv.imwrite("pano.png", pano)
plt.imshow(pano)
plt.show()
