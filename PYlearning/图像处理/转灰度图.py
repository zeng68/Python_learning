import numpy as np
import cv2
img = cv2.imread('C:\\Users\\Administrator\\Desktop\\PYlearning\\123.png',1)
img1 = cv2.imread('E:\\a4.jpg',0)
# 转化为灰度值图像
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.114, 0.587, 0.299])
gray = rgb2gray(img)#灰度图

print("aaa")