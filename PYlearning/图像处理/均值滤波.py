from PIL import Image
import numpy as np
path = "E:\\LennaSaltNoise.jpg"#图像路径
SIZE = 3#卷积核大小
padding = SIZE//2#四个方向需要加的padding大小


"""*************************************    均值滤波   ********************************************
        把（x,y）像素周围卷积核大小内的像素累加后，返回一个int类型均值
"""
#均值滤波函数
def MeanFilter(temp,x, y,SIZE):
    sum = 0
    for X in range(SIZE):
        for Y in range(SIZE):
            sum = sum+temp[x+X][y+Y]
    return int(sum/(SIZE*SIZE))

"""*******************************           START         *******************************"""
#img = Image.open("E:\\a2.jpg").convert('L')#读取图片并转为灰度图
img = Image.open(path).convert('L')#读取图片并转为灰度图
img2 = img.copy()
pixel = img.load()
w,h = img.size#列 行

#生成一个带有padding的模板图像
TempArry = np.zeros([h+padding*2,w+padding*2],np.uint8)#生成一个和图像对应的加入padding的空白模板
TempArry[padding:h+padding,padding:w+padding] = img#把图像嵌入空白模板的padding内

#循环对像素进行逐像素均值滤波
for x in range(0,h):
    for y in range(0,w):
           pixel[y,x] = MeanFilter(TempArry,x,y,3)

#img2.show()#原图
img.show()#均值滤波











