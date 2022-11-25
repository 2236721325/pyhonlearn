#图像填充
import cv2 as cv
img=cv.imread("images/img1.png")
top_size,bottom_size,left_size,right_size=(50,50,50,50)
replicate=cv.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv.BORDER_REPLICATE)

cv.imshow("replicate",replicate)

cv.waitKey(0)
