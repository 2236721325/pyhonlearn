import cv2 as cv
import numpy as np
## 图像加法
import sys
img1=cv.imread("images/img1.png")
img2=cv.imread("images/img2.png")
print(img2.shape)
img2=cv.resize(img2,(img1.shape[1],img1.shape[0]))

cv.imshow("bigImg2",img2)
cv.imshow("bigImg1",img1)

print(img1.shape)
print(img2.shape)

showImg1=cv.add(img1,img2)

cv.imshow("showImg1",showImg1)


showImg2=cv.addWeighted(img1,0.5,img2,0.5,0)

cv.imshow("showImg2",showImg2)
cv.waitKey(0)


