import numpy as np
import cv2
import bisect
# 计算累计概率分布Pr
def get_Sk(Hist):
    sum_Hist = sum(Hist)
    Pr = Hist / sum_Hist
    # 计算累计概率Sk
    Sk = []
    temp = 0
    for n in Pr:
        sk = temp + n
        Sk.append(sk)
        temp = sk
    Sk = np.asarray(Sk)
    return Sk

#映射表   sk1(原图概率密度)  sk2(目标图概率密度)
def get_lut(sk1, sk2):
    index = np.zeros(256,dtype='uint8')
    a=0
    for i in np.nditer(sk1):
        subscript = bisect.bisect_right(sk2, i)
        if subscript >=256:#防止二分查找出现256下标越界
            subscript = 255
        if abs(sk2[subscript]-i) < abs(sk2[subscript-1]-i):
            index[a] = subscript
        else:
            index[a] = subscript -1
        a = a+1
    return index
"""*************************************          START             ******************************************"""
Src = cv2.imread("E:\\MV.jpg",0)
Dist = cv2.imread("E:\\car.jpg",0)

#1.获取原图和目标图直方图信息
SrcHist = cv2.calcHist([Src],[0],None,[256],[0,255])
DistHist = cv2.calcHist([Dist],[0],None,[256],[0,255])

#2.计算原图直方图和目标图各灰度级累计概率密度
pr = get_Sk(SrcHist)
pz = get_Sk(DistHist)

#3.生成 原图直方图累计概率密度 和目标直方图累计概率密度单映射表
SML = get_lut(pr,pz)



#4.遍历图像各个灰度值，完成原图直方图到目标直方图类型的映射
h,w = Src.shape#列 行
ImgOutput = Src.copy()
for i in range(0,h):
    for j in range(0,w):
        ImgOutput[i][j] =SML[ImgOutput[i][j]]


cv2.imshow("OUT",ImgOutput)
cv2.imshow("Src",Src)
cv2.imshow("Car",Dist)
cv2.waitKey()






