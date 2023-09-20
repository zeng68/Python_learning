import cv2
from PIL import Image
import numpy as np
path = "E:\\LennaSaltNoise.jpg"#图像路径

SIZE = 3#卷积核大小
padding = SIZE//2#四个方向需要加的padding大小

def Middle(temp,x, y,SIZE):
    #Mask = np.zeros([SIZE,SIZE],np.uint8)#临时卷积核
    s = []#把(x,y)周围像素（也就是对应卷积区域）的像素放入列表s
    for X in range(SIZE):
        for Y in range(SIZE):
            #Mask[X,Y] = temp[x+X][y+Y]
            s.append(temp[x+X][y+Y])
    s.sort()
    #print(x, y)
    return int(s[SIZE*SIZE//2+1])#返回中位数

"""***********************************************           START         ***********************************************************"""
#img = Image.open("E:\\a2.jpg").convert('L')#读取图片并转为灰度图
#img = Image.open(path).convert('L')#读取图片并转为灰度图
img = cv2.imread(path,0)
pixel = img.load()
w,h = img.size#列 行

#生成一个带有padding的临时模板图像
TempArry = np.zeros([h+padding*2,w+padding*2])#生成一个和图像对应的加入padding的空白模板
TempArry[padding:h+padding,padding:w+padding] = img#把图像嵌入空白模板的padding内

#循环对像素进行逐像素中值滤波
for x in range(0,h):
    for y in range(0,w):
           pixel[y,x] = Middle(TempArry,x,y,3)

img.show()












