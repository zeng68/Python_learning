"""
****************************************************通道分离与合并***********************************************


import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)#控制台输出打印完全展示图像的各个通道信息所依赖的函数


# 1.读入图像
img1 = cv2.imread("F:\\aaa\\5.jpg",1)#读取彩色图BGR三通道图
#cv2.namedWindow("img1")
#cv2.imshow('img1',img1)


# 2.BGR图像三通道分离
b, g, r = cv2.split(img1)#b=img1[:,:,0] g=img1[:,:,1] r = img1[:,:,2] 或 b=cv2.split(img1)[0] g = cv2.split(img1)[1] r=cv2.split(a)[2]
cv2.imshow("blue", b)#输出蓝色信息
cv2.imshow("green", g)#输出绿色通道信息
cv2.imshow("red", r)#输出红色通道的信息

# 3.BGR图像三通道合并
Mge = cv2.merge([b,g,r])#bgr三通道合并函数
cv2.imshow("merge",Mge)


cv2.waitKey(0)
cv2.destroyAllWindows()

"""











