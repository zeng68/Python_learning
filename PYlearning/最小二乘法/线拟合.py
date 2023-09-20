import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 5, 6, 7, 8])
A = np.vstack([x, np.ones(len(x))]).T  # 按照垂直方向上堆叠，然后再进行转置
print(A)
# [[1. 1.]
#  [2. 1.]
#  [3. 1.]
#  [4. 1.]
#  [5. 1.]]

m, c = np.linalg.lstsq(A, y, rcond=None)[0]
print(m, c)





# 计算回归系数
coefficients = np.polyfit(x, y, 1)  # 1表示拟合线是一次多项式
# 提取回归系数中的斜率和截距
m = coefficients[0]  # 斜率
c = coefficients[1]  # 截距

print(m, c)

