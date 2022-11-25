import cv2 as cv
import numpy as np

#https://www.jianshu.com/p/9142bb5e416a
# 卷积运算
img=cv.imread("images/noise_img.png")
cv.imshow("img",img)

# 定义卷积核
kernel = np.ones((5, 5), np.float32) / 25
# 卷积操作，-1表示通道数与原图相同
dst = cv.filter2D(img, -1, kernel)
# 两张图片横向合并，便于对比显示
result = np.hstack((img,dst))

cv.imshow('result',result)
# 图像平滑处理
# 图像去噪
#均值滤波
#简单的平均卷积操作
blur=cv.blur(img,(5,5))

# 方框滤波
# 跟均值滤波一样 只不过可以多选一个参数 可以归一化
box_filter=cv.boxFilter(img,-1,(5,5),normalize=True)
cv.imshow("blur",blur)
cv.imshow("box_filter",box_filter)


# 高斯滤波
gausian_filter = cv.GaussianBlur(img,(5,5),0)

cv.imshow("gausian_filter",gausian_filter)

median_filter = cv.medianBlur(img,5)


cv.imshow("median_filter",median_filter)

result = np.hstack((box_filter,gausian_filter,median_filter))
cv.imshow("result",result)



cv.waitKey(0)
cv.destroyAllWindows()