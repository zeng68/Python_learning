import math
import numpy as np
from PIL import Image
import cv2
path = "C:\\Users\\Administrator\\Desktop\\MV.jpg" #图像读取路径
path1 = "E:\\GaussianBlur.jpg"#图像存放路径
sigma = 0.1

""""
*************************************  一.高斯卷积核   *********************************************
"""
# 1.高斯卷积核初步自动形成
R =1#卷积核大小 Size = (R*2+1)^2
#Mask = [[4,3,2,3,4],[3,2,1,2,3],[2,1,0,1,2],[3,2,1,2,3],[4,3,2,3,4]]
Mask = [[abs(x)+abs(y) for y in range(-R,R+1)] for x in range(-R,R+1)]#使用循环自动初步形成卷积核
#print(Mask)
#print(type(Mask))
#print(Mask)

#2.高斯函数处理生成归一化高斯卷积核
def Gaussian(x):
    return 1/(sigma*(2*math.pi)**0.5)*math.exp(-(x**2)/2*sigma**2)#高斯函数
Mask = np.array([list(map(Gaussian,a)) for a in Mask])#map(function,iterable)第二个参数作为第一个函数参数进行计算，返回一个迭代器，用list()转换为列表
#print(Mask)
Mask =Mask/sum(sum(Mask))#卷积核归一化
#print(Mask)

""""
****************** *************** 二.卷积函数（输入图像与Mask卷积核进行卷积）   *************************
"""
#卷积函数
def Conv(A,Mask):
    L = len(Mask)#卷积核的大小
    S = np.array([0,0,0])
    for x in range(L):#S数组三个元素（三通道）对Mask同时卷积
        for y in range(L):
            S = S + A[x][y]*Mask[L-x-1][L-y-1]
    return tuple(S.round().astype(int))

#获取像素（x,y）周围区域
def GetMatrix(pixel,x, y):  # 获取待模糊像素（x，y）Mask大小的模糊区域（三通道）
    for X in range(L + 1):#l全局变量58行的
        for Y in range(L + 1):
            TempM[L + X][L + Y] = np.array(pixel[x + X, y + Y])
            TempM[L - X][L + Y] = np.array(pixel[x - X, y + Y])
            TempM[L + X][L - Y] = np.array(pixel[x + X, y - Y])
            TempM[L - X][L - Y] = np.array(pixel[x - X, y - Y])
    return np.array(TempM)

"""
******************************************************    START      **************************************************
"""
img = Image.open(path)
#img2 = Image.open(r'C:\Users\Administrator\Desktop\MV.jpg')#原图
img2 = cv2.imread(path)
pixel = img.load()
pixelCopy = img.load()
Rect = ((0,0), (150,280))  # 选择模糊区域（矩形区域）
L = int((len(Mask) - 1) / 2)#Mask长度
TempM = [list(M) for M in Mask]#生成Mask的一个临时列表类型核

#对待卷积区域Rect = ((0,0), (150,280))进行逐像素卷积
for x in range(Rect[0][0],Rect[1][0]):
    for y in range(Rect[0][1],Rect[1][1]):
        pixel[x,y] = Conv(GetMatrix(pixelCopy,x,y), Mask)#修改原图像素为卷积后的像素
img.show()
img.save(path1)
