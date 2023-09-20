import numpy as np
import cv2
# 读入  灰度图
img: np.ndarray = cv2.imread("E:MV.jpg")
img = img[:, :, 0]
cv2.imshow("before", img)
cv2.waitKey(0)

# 预处理
h ,w =img.shape
b = np.mean(img,axis=0)
STD = np.std(img,axis=0)
img = img-b
img = img/STD



img_T = img.transpose()
Mat = img_T.dot(img)  # 得到 X * X_T


# 求 X * X_T 的前k大特征向量
eigvals, vecs = np.linalg.eig(Mat)  # 注意求出的eigvals是特征值，vecs是标准化后的特征向量
indexs = np.argsort(eigvals)
indexs = indexs[::-1]
print(eigvals.shape)


# 编码矩阵 D 是前k大特征向量组成的矩阵(正交矩阵)——topk_evecs
k = 64
topk_evecs:np.ndarray = vecs[:,indexs[0:k]]
print(topk_evecs.shape)

# X * D = 维度压缩后的图片信息——encode  （信息由 512 x 512 压缩为 512 x 64）
encode = img.dot(topk_evecs)

# 译码矩阵即 D_T
img_new = ((encode.dot(topk_evecs.transpose())*STD) +b ).astype(np.uint8)  # 译码得到的新图片
print(img_new)
img_new[img_new < 0] = 0
img_new[img_new > 255] = 255

cv2.imshow("after", img_new)
cv2.waitKey(0)