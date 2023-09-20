# import torch as t
# from torch import nn
#
# # in_features由输入张量的形状决定，out_features则决定了输出张量的形状
# connected_layer = nn.Linear(in_features = 64*64*3, out_features = 1)
#
# # 假定输入的图像形状为[64,64,3]
# input = t.randn(2,64,64,3)
#
# # 将四维张量转换为二维张量之后，才能作为全连接层的输入
# input = input.view(2,64*64*3)
# print(input.shape)
# output = connected_layer(input) # 调用全连接层
# print(output.shape)


import numpy as np
import cv2

# def colorize_segmentation(seg, palette):
#     color_seg = np.zeros((seg.shape[0], seg.shape[1], 3), dtype=np.uint8)  # 渲染图画板
#     for label, color in enumerate(palette):
#         color_seg[seg == label, :] = color
#     return color_seg
#
#
# # 假设 seg 是形状为 (height, width) 的分割图像，palette 是颜色调色板
# seg = cv2.imread(r'C:\Users\Administrator\Desktop\PYlearning\gggggg.jpg', cv2.IMREAD_GRAYSCALE)
# palette = [(255, 0, 0), (0, 100, 0), (0, 0, 255)]  # 示例调色板
#
# # 生成彩色分割图像
# color_seg = colorize_segmentation(seg, palette)
# cv2.imshow('img',color_seg)
# cv2.waitKey()
# # 进行可视化或其他后续处理


# import cv2
# import numpy as np
#
# # 读取单通道图像
# image = cv2.imread('gggggg.jpg', 0)
#
# # 预处理，将不同类别的像素值分别二值化为255，其他像素值为0
# binary_image = np.zeros_like(image)
# binary_image[image == 255] = 255
# binary_image[image == 254] = 255
# binary_image[image == 253] = 255
# binary_image[image == 252] = 255
#
# # 轮廓检测
# contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# # 绘制轮廓
# contour_image = np.zeros_like(image)
# cv2.drawContours(contour_image, contours, -1, (255, 255, 255), thickness=1)
#
# # 显示结果
# cv2.imshow('Contour Image', contour_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np
#
# # 读取灰度图像
# image = cv2.imread(r'C:\Users\Administrator\Desktop\PYlearning\gggggg.jpg', 0)
#
# # 获取图像中的唯一像素值
# unique_values = np.unique(image)
#
# # 存放轮廓的列表
# contour_list = []
#
# # 遍历每个像素值类别
# for value in unique_values:
#     # 创建临时二值图像
#     binary_image = np.zeros_like(image)
#     binary_image[image == value] = 255
#
#     # 轮廓检测
#     contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     # 将轮廓添加到列表
#     contour_list.append(contours)
#
# # 打印每个类别的轮廓数量
# for i, contours in enumerate(contour_list):
#     print("类别", unique_values[i], "的轮廓数量:", len(contours))






