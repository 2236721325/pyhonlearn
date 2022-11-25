import cv2 as cv
import numpy as np
import sys
# 位运算 实现扣图
img1=cv.imread("images/img1.png")
logo=cv.imread("images/logo.png")

img2=cv.resize(logo,(200,200))

#我想在左上角放置一个logo，所以我创建了一个 ROI,并且这个ROI的宽和高为我想放置的logo的宽和高
rows,cols,channels = img2.shape
roi = img1 [0:rows,0:cols]
#现在创建一个logo的掩码，通过对logo图像进行阈值，并对阈值结果并创建其反转掩码
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
cv.imshow("img2gray",img2gray)
ret,mask = cv.threshold(img2gray,225,255,cv.THRESH_BINARY)
cv.imshow("mask",mask)
mask_inv = cv.bitwise_not(mask)
cv.imshow("mask_inv",mask_inv)

#现在使 ROI 中的徽标区域变黑
img1_bg = cv.bitwise_and(roi,roi,mask = mask)
cv.imshow("img1_bg",img1_bg)
#仅从徽标图像中获取徽标区域。
img2_fg = cv.bitwise_and(img2,img2,mask = mask_inv)
#在 ROI 中放置徽标并修改主图像

cv.imshow("img2_fg",img2_fg)
dst = cv.add(img1_bg,img2_fg)
img1 [0:rows,0:cols] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()



