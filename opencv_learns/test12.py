# 图片阙值

import cv2 as cv

logo=cv.imread("images/logo.png")

logo_gray=cv.cvtColor(logo,cv.COLOR_BGR2GRAY)

cv.imshow("logo_gray",logo_gray)

ret,dst_binary=cv.threshold(logo_gray,225,255,cv.THRESH_BINARY)
ret,dst_binary_inv=cv.threshold(logo_gray,225,255,cv.THRESH_BINARY_INV)
ret,dst_trunc = cv.threshold(logo_gray,225,255,cv.THRESH_TRUNC)
#大于阙值就是阙值 否则不变
ret,dst_tozero = cv.threshold(logo_gray,225,255,cv.THRESH_TOZERO)
#大于阙值不改变否则为0
ret,dst_tozero_inv = cv.threshold(logo_gray,225,255,cv.THRESH_TOZERO_INV)


cv.imshow("dst_binary",dst_binary)
cv.imshow("dst_binary_inv",dst_binary_inv)
cv.imshow("dst_trunc",dst_trunc)
cv.imshow("dst_tozero",dst_tozero)
cv.imshow("dst_tozero_inv",dst_tozero_inv)


cv.waitKey(0)