
import numpy as np
import cv2 as cv
# n_img=cv.imread("images/noise_img.png",cv.IMREAD_GRAYSCALE)

# n_grad=cv.Sobel(n_img,cv.CV_64F,1,1,ksize=3)
# n_grad=cv.convertScaleAbs(n_grad)


# cv.imshow("n_image",n_grad)

n_img=cv.imread("images/noise_img.png",cv.IMREAD_GRAYSCALE)
n_img=cv.blur(n_img,(5,5))
cv.imshow("r_noise",n_img)

n_grad_x=cv.Sobel(n_img,cv.CV_64F,1,0,ksize=3)
n_grad_y=cv.Sobel(n_img,cv.CV_64F,0,1,ksize=3)

n_grad_x=cv.convertScaleAbs(n_grad_x)
n_grad_y=cv.convertScaleAbs(n_grad_y)
n_grad=cv.addWeighted(n_grad_x,0.5,n_grad_y,0.5,0)

ret,mask=cv.threshold(n_grad,10,255,cv.THRESH_BINARY)



cv.imshow("n_image",mask)


cv.waitKey(0)