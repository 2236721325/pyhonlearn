# 在本教程中：

# 我们将学习不同的形态操作，如腐蚀、膨胀、开、闭等。
# 我们将看到不同的函数，如： cv.erode()**、 **cv.dilate()**、 **cv.morphologyEx() 等。
import cv2 as cv
import  numpy as np
img=cv.imread("images/img3.png")

kernel=np.ones((3,3),np.uint8)
erosion = cv.erode(img,kernel,iterations=1)
dilation = cv.dilate(img,kernel,iterations = 1)

result=np.vstack((img,erosion,dilation))

cv.imshow("result",result)




#剩余略
cv.waitKey(0)
