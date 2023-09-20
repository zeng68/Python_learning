import numpy as np
import cv2

#1. 读入度图
Src = cv2.imread("E:/MV.jpg",0)# 287 *450
img = cv2.imread("E:/MV.jpg",0)


#2 预处理(图像行为主成分分析，列作为样本)
h ,w =img.shape
avg = np.mean(img,axis=0)#压缩行 求均值
STD = np.std(img,axis=0)#标准差
img = img-avg
img = img/STD

img_T = img.T#矩阵转置
Mat = img_T.dot(img)#450 * 450

# 求 Mat  的前k大特征向量
eigvals, vecs = np.linalg.eig(Mat)  # eigvals是特征值，vecs特征向量
indexs = np.argsort(eigvals)#特征值数组eigvals从小到大排列并返回从小到大排列后原数组的下标
indexs = indexs[::-1]#从大到小排列后原数组的下标
print(eigvals.shape)


# 编码矩阵  是前k大特征向量组成的矩阵
k = w//2#特征向量的大小为图像宽度的一半（k应低于特征值的个数）
k = 100
topk_evecs = vecs[:,indexs[0:k]]#  取前K大特征值对应的特征向量  P矩阵 450行 30列
print(topk_evecs.shape)


# 维度压缩后的图片信息—encode
encode = img.dot(topk_evecs)# 287 *30

# 译码矩阵
img_new = encode.dot(topk_evecs.T)
img_new = (img_new * STD + avg).astype(np.uint8)  # 译码得到的新图片
print(img_new)



cv2.imshow("after", img_new)
cv2.imshow("Src", Src)
cv2.waitKey(0)