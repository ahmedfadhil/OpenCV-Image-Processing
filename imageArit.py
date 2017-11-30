import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

# add = img1 + img2
# added pixel values
# add = cv2.add(img1,img2)
# adding weighted values
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# cv2.imshow('weighted', weighted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
img2grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2grey, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.imshow('mask inverse', mask_inv)
cv2.imshow('image1 bg', img1_bg)
cv2.imshow('image2 fg', img2_fg)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
