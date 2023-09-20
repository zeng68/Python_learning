import numpy as np
import cv2 as cv

# 图像预处理（放到数组中像素个数行5列的数组中）
def mean_shift(img):
    rows, cols, channel = img.shape
    rgb_array = np.zeros((rows * cols, 5))# (rows*cols)行   5列（RGBxy）  每一行保存一个像素点的信息
    dstimg = np.zeros((rows, cols, channel))#原图同大小同深度的空白图像


    k = 0
    #遍历图像把每个像素点三通道RGB和坐标xy放入数组
    for i in range(0, rows):
        for j in range(0, cols):
            rgb_array[k][0], rgb_array[k][1], rgb_array[k][2], rgb_array[k][3], rgb_array[k][4] = img[i][j][0], img[i][j][1], img[i][j][2], i, j
            k += 1

# 聚类的圆形半径与收敛条件
    r = 60# r是每次圆形聚类的半径
    convergence = 50#每次圆形聚类收敛的条件   （中心点代替此次聚类半径中所有点）



    temp_point = []#临时存放中心点r半径内所有像素点信息
    #初始化标签flag，用来控制是否初始化中心点坐标
    flag = False
    while rgb_array.shape[0] != 0:
        #在rows*cols个像素点中随机找出一个作为初始化中心点
        if flag == False:
            index_row = np.random.randint(0, rgb_array.shape[0])  # 任意寻找一个点作为开始的点
            mean_r = rgb_array[index_row][0]
            mean_g = rgb_array[index_row][1]
            mean_b = rgb_array[index_row][2]
            mean_x = rgb_array[index_row][3]
            mean_y = rgb_array[index_row][4]

        #对每个像素点进行遍历，找出在空间r内的点，
        #并将像素值记录在temp_point中，下标信息记录在index中
        index = []
        for i in range(0, rgb_array.shape[0]):#按行遍历
            #（该点到中心点的距离）（像素点的五个信息全部参与运算这样会更精确一些）
            L = ((rgb_array[i][0] - mean_r) ** 2 + (rgb_array[i][1] - mean_g) ** 2 +(rgb_array[i][2] - mean_b) ** 2 + (rgb_array[i][3] - mean_x) ** 2 + (rgb_array[i][4] - mean_y) ** 2) ** 0.5

            if L <= r:#该像素点在球半径r内，距离<所定半径
                temp_point.append(rgb_array[i])#把符合条件的像素点信息与坐标储存起来
                index.append(i)

        #判断半径r内是否有像素点
        if len(temp_point) > 0:
            element0, element1, element2,element3, element4 = 0, 0, 0, 0, 0

            #求偏移距离
            #步骤：step1：将所有在半径内的像素点求和
            #     step2：对求和向量均值化，得到需要移动到终点
            #     step3：对均值化的求和向量减去中心点向量的模得到偏移距离(判断接下来是否进行漂移)

            # step1 向量求和(半径r范围内所有像素点点的五行一列的点向量求和)
            for i in range(0, len(temp_point)):
                element0 += temp_point[i][0]
                element1 += temp_point[i][1]
                element2 += temp_point[i][2]
                element3 += temp_point[i][3]
                element4 += temp_point[i][4]
            # step2 求和向量均值化，得到需要移动到终点坐标
            element0 = element0 / len( temp_point)
            element1 = element1 / len(temp_point)
            element2 = element2 / len(temp_point)
            element3 = element3 / len(temp_point)
            element4 = element4 / len(temp_point)

            # step2 终点坐标减去中心点向量取距离得偏移距离
            new_L = ((element0 - mean_r) ** 2 + (element1 - mean_g) ** 2 + (element2 - mean_b) ** 2 + (element3 - mean_x) ** 2 + (element4 - mean_y) ** 2) ** 0.5

            #偏移距离超参
                        #小于convergence，停止漂移，并将原图中所有半径<r像素点用中心点去替代他们，并赋值给空白图像dstimg
                        #大于convergence，继续漂移中心点继续更新

            # step3 偏移距离小于等于convergence停止漂移
            if new_L <= convergence:
                for i in range(0, len(index)):
                    #返回原图片对应的行列，在新图的相同位置使用终点位置值代替
                    row = int((temp_point[i])[3])
                    col = int((temp_point[i])[4])
                    dstimg[row][col][0] = element0
                    dstimg[row][col][1] = element1
                    dstimg[row][col][2] = element2

                rgb_array = np.delete(rgb_array, index, 0)#按行删除（index储存的就是要删除的每一行）
                flag = False
            #中心点更新
            else:
                mean_r = element0
                mean_g = element1
                mean_b = element2
                mean_x = element3
                mean_y = element4
                flag = True
        #清空上一轮r半径的漂移，准备下一轮
        temp_point = []

    #将dstimg像素值大小规定在 0-255范围内
    dstimg = np.array(dstimg, np.uint8)
    return dstimg


src = cv.imread("E:\\home.jpg")
#src2 = dist = cv.bilateralFilter(src, 0, 40, 15)
img = mean_shift(src)
#img2 = mean_shift(src2)
cv.imshow("Out",img)
#cv.imshow("Out2",img2)
cv.waitKey()



