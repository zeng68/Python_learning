import numpy as np
from skimage.measure import compare_ssim


# 计算psnr
def psnr(imag1, imag2):
    diff = imag1 - imag2
    # print(np.sum(diff))
    mse = np.mean(np.square(diff))
    psnr = 10 * np.log10(255 * 255 / mse)
    return (psnr)


# 计算ssim
def ssim(imag1, imag2):
    (grayScore, diff) = compare_ssim(imag1, imag2, full=True)
    # diff = (diff * 255).astype("uint8")
    return grayScore


# 读入载体图片和水印图片
Carrier = Image.open('carrier.png')
WaterMark = Image.open('watermark.png')
# 确认需要隐藏在二进制位第几位
Layers = int(input('请输入要隐藏在第几层（0-7）：'))

# 将读入的图片转为array类型
Carrier_array = np.array(Carrier)
WaterMark_array = np.array(WaterMark)

a, b = WaterMark_array.shape
a1, b1 = Carrier_array.shape

array1 = np.zeros((a, b), dtype='float32')
# 构建水印大小数组，将载体同等大小位传入
for i in range(a):
    for j in range(b):
        array1[i][j] = Carrier_array[i][j]
# 嵌入水印
for i in range(a):
    for j in range(b):
        w = Carrier_array[i][j] // (2 ** Layers)
        if w % 2 == 0 and WaterMark_array[i][j] == 1:
            Carrier_array[i][j] = Carrier_array[i][j] + (2 ** Layers)
        elif w % 2 == 1 and WaterMark_array[i][j] == 0:
            Carrier_array[i][j] = Carrier_array[i][j] - (2 ** Layers)

# 构建水印大小数组，将嵌入水印后的载体的同等大小位传入
array2 = np.zeros((a, b), dtype='float32')
for i in range(a):
    for j in range(b):
        array2[i][j] = Carrier_array[i][j]

# 计算psnr
PSNR = psnr(array1, array2)
# PSNR = skimage.measure.compare_psnr(Carrier_array1, Carrier_array, 255)
print('峰值信噪比（PSNR）为：', PSNR)
# 计算ssim
SSIM = ssim(array1, array2)
print('结构相似性（SSIM）为：', SSIM)

# 展示嵌入水印后的图片
I = Image.fromarray(Carrier_array)
I.show()

# 提取水印
a1, b1 = Carrier_array.shape
WaterMark_array1 = np.zeros((a1, b1), dtype='int8')
for i in range(a1):
    for j in range(b1):
        w = Carrier_array[i][j] // (2 ** Layers)
        if w % 2 == 1:
            WaterMark_array1[i][j] = 1

# 将提取的水印图像输出
WaterMark_array1.dtype = 'bool'
# print(WaterMark_array1.shape)
I = Image.fromarray(WaterMark_array1)
I.show()