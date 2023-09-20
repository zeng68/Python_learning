import cv2
import numpy as np

# 读取灰度图像
image = cv2.imread('rectangle.png', 0)

# 去重后获取图像中的唯一像素值
unique_values = np.unique(image)

# 存放轮廓的列表
contour_list = []

# 遍历每个像素值类别
for value in unique_values:
    # 创建临时二值图像
    binary_image = np.zeros_like(image)
    binary_image[image == value] = 255
    # 轮廓检测
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 将轮廓添加到列表
    contour_list.append(contours)

drawing_board = np.zeros_like(image)
# 打印每个类别的轮廓数量
for i, contours in enumerate(contour_list):
    print("类别", unique_values[i], "的轮廓数量:", len(contours))
    cv2.drawContours(drawing_board, contours, -1, (255, 255, 255), 2)
cv2.imshow("my", drawing_board)
cv2.waitKey()
