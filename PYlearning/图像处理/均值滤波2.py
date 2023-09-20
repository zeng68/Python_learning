import cv2
from PIL import Image
import numpy as np
path = "E:\\LennaSaltNoise.jpg"#图像路径

SIZE = 5#卷积核大小
padding = SIZE//2#四个方向需要加的padding大小

def Middle(temp,x, y,SIZE):
    sum = 0
    for X in range(SIZE):
        for Y in range(SIZE):
            sum+=temp[x+X][y+Y]
    return round(sum/(SIZE*SIZE))#返回平均数(四舍五入)


"""***********************************************           START         ***********************************************************"""
#img = Image.open("E:\\a2.jpg").convert('L')#读取图片并转为灰度图
#img = Image.open(path).convert('L')#读取图片并转为灰度图
img = cv2.imread(path,0)
img2 =cv2.imread(path,0)
h,w = img.shape#行 列

#生成一个带有padding的临时模板图像
TempArry = np.zeros([h+padding*2,w+padding*2])#生成一个和图像对应的加入padding的空白模板
TempArry[padding:h+padding,padding:w+padding] = img#把图像嵌入空白模板的padding内

#循环对像素进行逐像素中值滤波
for x in range(0,h):
    for y in range(0,w):
           img[x,y] = Middle(TempArry,x,y,SIZE)#卷积后的中位数赋值给原灰度图像素




cv2.imshow("Middle",img)
cv2.imshow("SRC",img2)
cv2.waitKey()












