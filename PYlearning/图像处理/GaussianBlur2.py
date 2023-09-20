import cv2
import numpy as np
import math
SIZE = 5#卷积核大小（只能为基数）
padding = SIZE//2
R = SIZE//2
sigma = 1


#高斯卷积核设计
Mask = [[abs(x)+abs(y) for y in range(-R,R+1)] for x in range(-R,R+1)]
for i in range(0,SIZE):
    for j in range(0,SIZE):
        Mask[i][j] = 1/(sigma*(2*math.pi)**0.5)*math.exp(-(Mask[i][j]**2)/2*sigma**2)#高斯函数处理
Mask = np.array(Mask)
Mask =Mask/sum(sum(Mask))#卷积核归一化
print("a")
""""
            TmMask2   带有padding和img的模板
            x,y为TmMask2映射到Temp的像素偏移量  
"""
# 获取待模糊像素（x，y）附近Mask大小的像素区域
def GetMatrix(TmMask2,x,y):
    Temp = np.zeros([SIZE,SIZE],np.uint8)
    for X in range(SIZE):
        for Y in range(SIZE):
            Temp[X][Y] = TmMask2[x+X][y+Y]
    return np.array(Temp)#返回需要卷积的区域副本


"""               ****减少运算废弃的卷积函数*****
def Conv(A,Mask):
    SUM =0
    for x in range(SIZE):
        for y in range(SIZE):
            SUM = SUM +A[x][y]*Mask[x][y]
    return int(SUM)
"""
"""***********************      一.读取图像                  ************************************"""
img = cv2.imread("E:\\Lenna1.jpg",0)
img2 = cv2.imread("E:\\Lenna1.jpg",0)

#img = np.dot(img[..., :3], [0.299, 0.587, 0.114])
#img=np.array(img,dtype="uint8")
#cv2.imshow("原灰度图",d)
#cv2.waitKey()

h,w = img.shape#高度 宽度
"""***********************     二.制作padding模板             ************************************"""
TmMask = np.zeros([h+padding*2,w+padding*2])
TmMask[padding:h+padding,padding:w+padding] = img#把图像嵌入空白模板TmMask的padding内

"""***********************     三.卷积并修改原灰度图的像素值     ************************************"""
#对img每个像素循环卷积修改img图像数组中的值
for x in range(h):
    for y in range(w):
        #img[x-padding][y-padding] = Conv(GetMatrix(TmMask,x,y), Mask)#修改原图像素为卷积后的像素
        #卷积（数组相乘）并修改原图像素
        img[x][y] = np.sum(GetMatrix(TmMask, x, y) * Mask)#数组相乘比上一行自己写Conv()函数数组元素通过循环相乘高效

""" ***********************     四.高斯平滑后与原灰度图输出     ************************************"""
cv2.imshow("Gaussian",img)
cv2.imshow("SRC",img2)
cv2.waitKey()