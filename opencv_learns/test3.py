import cv2 as cv
import numpy as np
import sys
dir=sys.path[0]
image = cv.imread(f"{dir}/MyPic.jpg")

print(image.shape)
face=image[50:250,50:250]
cv.imshow("hehl",face)
cv.waitKey(0)
print(image)
