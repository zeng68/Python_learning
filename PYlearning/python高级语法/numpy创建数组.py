import numpy as np

# 用一维数组创建
a = np.array([1, 2, 3, 4, 5])
print(a)
print(a.dtype)  # 元素类型

# 1.用元组创建
b = np.array((1, 2, 3, 4, 5))
print(b)

# 2.多维数组
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(c.ndim)  # 查看维度


d = np.array([[[1, 2, 3], [4, 5, 6, ], [7, 8, 9], [1, 2, 1]]])
print(d)
print(d.shape)  # 每一维的大小(1,4,3)，第一维3,第二维4，第三维,1
print(d.size) # 元素个数
print(d.itemsize)# 每个元素所占的字节数

# 3.zeros 函数创建指定长度火车形状的全零数组
e = np.zeros((2,3))
print(e)

# 4. ones 函数 创建指定长度或者形状全为1的数组
f = np.ones((2,4))
print(f)

# 5. empty函数 创建一个没有任何具体值的数组
g = np.empty((3,1))
print(g)


