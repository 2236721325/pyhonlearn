import cv2 as cv
import numpy as np
# 图像梯度
img = np.zeros((512, 512, 3), np.uint8)


img=cv.circle(img,(256,256),200,(255,255,255),-1)

gradx=cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
grady=cv.Sobel(img,cv.CV_64F,0,1,ksize=3)

gradx=cv.convertScaleAbs(gradx)
grady=cv.convertScaleAbs(grady)

grad=cv.addWeighted(gradx,0.5,grady,0.5,0)
result=np.hstack((img,gradx,grady))
cv.imshow("result",result)

cv.imshow("grad",grad)

grad_all=cv.Sobel(img,cv.CV_64F,1,1,ksize=3)
grad_all=cv.convertScaleAbs(grad_all)
cv.imshow("grad_all",grad_all)





cv.waitKey(0)
