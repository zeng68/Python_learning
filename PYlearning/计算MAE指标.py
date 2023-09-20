import cv2
import numpy as np

# cv2.imread()-------> (H W C)
# img_c = cv2.imread('E:\\GaussianBlur.jpg')
# h, w = img_c.shape[:2]

# 加载图像 A 和 B
img_a = cv2.imread('E:\\GaussianBlur.jpg', cv2.IMREAD_GRAYSCALE)
img_b = cv2.imread('E:\\GaussianBlur.jpg', cv2.IMREAD_GRAYSCALE)
h, w = img_a.shape[:2]

# 转换为 NumPy 数组，并将像素值映射到 0-1 范围内
img_a = np.array(img_a, dtype=np.float32) / 255.0
img_b = np.array(img_b, dtype=np.float32) / 255.0

# 计算两张图像的像素值差的绝对值，并将这些差值加起来
diff = np.abs(img_a - img_b)
mae = np.sum(diff) / (h * w)

# 打印 MAE 指标
print("MAE:", mae)
