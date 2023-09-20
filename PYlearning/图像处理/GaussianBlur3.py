import cv2
import numpy as np
import math
SIZE = 5#卷积核大小（只能为基数）
padding = SIZE//2
sigma = 3

#生成高斯卷积核（定卷积核中心坐标为（0，0））
GaussKernel =np.zeros((SIZE,SIZE))
for i in range(SIZE):
    for j in range(SIZE):
        xxAddyy = math.pow(i-padding,2)+math.pow(j-padding,2)
        GaussKernel[i,j] = math.exp(-xxAddyy / (2 * math.pow(sigma, 2))) / 2 * math.pi * math.pow(sigma, 2)
sum = np.sum(GaussKernel)
GaussKernel = GaussKernel / sum#归一化



""""
            TmMask2   带有padding和img的模板
            x,y为TmMask2映射到Temp的像素偏移量  
"""
# 获取待模糊像素（x，y）附近Mask大小的像素区域
def GetMatrix(TmMask2,x,y):
    Temp = np.zeros([SIZE,SIZE])
    for X in range(SIZE):
        for Y in range(SIZE):
            Temp[X][Y] = TmMask2[x+X][y+Y]
    return np.array(Temp)#返回需要卷积的区域副本


"""***********************      一.读取图像                  ************************************"""
path = "E:\\MV.jpg"
img = cv2.imread(path,0)
img2 = cv2.imread(path,0)
h,w = img.shape#高度 宽度
"""***********************     二.制作padding模板             ************************************"""
TmMask = np.zeros([h+padding*2,w+padding*2])
TmMask[padding:h+padding,padding:w+padding] = img#把图像嵌入空白模板TmMask的padding内

"""***********************     三.卷积并修改原灰度图的像素值     ************************************"""
#对img每个像素循环卷积修改img图像数组中的值
for x in range(h):
    for y in range(w):
        #卷积（数组相乘）并修改原图像素
        img[x][y] = np.sum(GetMatrix(TmMask, x, y) * GaussKernel)

""" ***********************     四.高斯平滑后与原灰度图输出     ************************************"""
cv2.imshow("Gaussian",img)
cv2.imshow("SRC",img2)
cv2.waitKey()
