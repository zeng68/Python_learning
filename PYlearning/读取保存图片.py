import cv2
# 读取图片并获取其大小信息
image1 = cv2.imread('E:\\GaussianBlur.jpg')
h, w, c = image1.shape
cv2.imwrite('example_saved.jpg', image1)


from PIL import Image
image2 = Image.open('E:\\GaussianBlur.jpg')
W, H = image2.size
C = image2.getbands()  # C('R','G','B')
image2.save('example_saved2.{}'.format('png'))  # img.save('example_saved.bmp', format='BMP')


import torch
import torchvision
# 生成一个 3x256x256 的随机张量
tensor = torch.rand(3, 256, 256)
# 将张量保存为 PNG 格式的图像文件
torchvision.utils.save_image(tensor, 'example2222.png')
