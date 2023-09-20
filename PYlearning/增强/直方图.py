# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
# from skimage import exposure
#
#
# import cv2
#
# # 读取图像
# image = cv2.imread(r'C:\Users\Administrator\Desktop\PYlearning\增强\灰度图1.jpg', 0)  # 以灰度模式读取图像
#
# # 进行直方图均衡化
# equalized_image_float = exposure.equalize_adapthist(image)
# equalized_image_uint8 = (equalized_image_float * 255).astype(np.uint8)
# # 显示均衡化后的灰度图
# cv2.imwrite('Equalized.jpg',equalized_image_uint8)
# # cv2.imshow('Equalized Image', equalized_image_float)
# # cv2.waitKey(0)
# cv2.destroyAllWindows()
#



import cv2
import numpy as np

# 读取图像
gray = cv2.imread(r'C:\Users\Administrator\Desktop\PYlearning\增强\灰度图1.jpg', 0)  # 以灰度模式读取图像

# 转换为灰度图像
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 高斯模糊
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# 计算高频成分（原始图像 - 模糊图像）
highpass = cv2.subtract(gray, blurred)

# 自适应增强
k = 0.2  # 增强系数（可以调整）
enhanced = cv2.addWeighted(gray, 1 + k, highpass, -k, 0)

cv2.imwrite('Equalized.jpg',enhanced)
# 显示增强后的图像
cv2.imshow("Enhanced Image", enhanced)
cv2.waitKey(0)
cv2.destroyAllWindows()
