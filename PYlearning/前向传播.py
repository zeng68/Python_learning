import numpy as np

# 初始化权重
weights = np.array([[[0.15, 0.20], [0.25, 0.30]], [[0.40, 0.45], [0.50, 0.55]]])

# 输入数据
l0 = np.array([[0.05], [0.10]])

# 偏置
bias = np.array([[.35], [0.60]])

# 真实值
y = np.array([[0.01], [0.99]])

# 学习率
i = 0.9

for j in range(10000):
    # 前向传播

    # 输入层---->隐含层
    temp1 = np.dot(weights[0], l0) + bias[0]
    l1 = 1 / (1 + np.exp(-temp1))
    # print("l1", l1)

    # 隐含层---->输出层：
    temp2 = np.dot(weights[1], l1) + bias[1]
    l2 = 1 / (1 + np.exp(-temp2))
    print("l2", l2)

    # 反向传播
    Error = 1 / 2.0 * (y - l2) ** 2
    # print("***************************************************")
    # print(l2)
    # print("Error", Error)

    # 隐含层---->输出层的权值更新
    TotalE = np.sum(Error)
    # print("TotalE", TotalE)

    alphaE1 = - (y - l2)
    alphaE2 = l2 * (1 - l2)
    alphaE3 = l1

    # print("alphaE1", alphaE1)
    # print("alphaE2", alphaE2)
    # print("alphaE3", alphaE3)

    alphaE = alphaE1 * alphaE2 * alphaE3
    # print("alphaE", alphaE)

    # 更新权重
    weightsT1 = weights[1] - i * alphaE
    # print("weightsT1", weightsT1)

    # 隐含层---->隐含层的权值更新：
    alphaE41 = alphaE1 * alphaE2
    alphaE42 = weights[1]
    alphaE4 = alphaE41 * alphaE42
    # print("alphaE41", alphaE41)
    # print("alphaE42", alphaE42)
    # print("alphaE4", alphaE4)

    alphaE4s = alphaE4[0] + alphaE4[1]
    # print("alphaE4s", alphaE4s)

    alphaE5 = l1 * (1 - l1)
    # print("alphaE5", alphaE5)

    alphaE6 = l0
    # print("alphaE6", alphaE6)

    alphaEE = alphaE4s * alphaE5 * alphaE6
    # print("alphaEE", alphaEE)

    # 更新权重
    weightsT2 = weights[0] - i * alphaEE
    # print("weightsT2", weightsT2)

    weights[0] = weightsT2
    weights[1] = weightsT1

# print(Error)
