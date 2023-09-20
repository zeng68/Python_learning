import cv2 as cv
"""
高斯双边模糊
bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None): 

    .   @param src Source 8-bit or floating-point, 1-channel or 3-channel image.
    .   @param dst Destination image of the same size and type as src .
    .   @param d Diameter of each pixel neighborhood that is used during filtering. If it is non-positive,
    .   it is computed from sigmaSpace.
    .   @param sigmaColor Filter sigma in the color space. A larger value of the parameter means that
    .   farther colors within the pixel neighborhood (see sigmaSpace) will be mixed together, resulting
    .   in larger areas of semi-equal color.
    .   @param sigmaSpace Filter sigma in the coordinate space. A larger value of the parameter means that
    .   farther pixels will influence each other as long as their colors are close enough (see sigmaColor
    .   ). When d\>0, it specifies the neighborhood size regardless of sigmaSpace. Otherwise, d is
    .   proportional to sigmaSpace.
    .   @param borderType border mode used to extrapolate pixels outside of the image, see #BorderTypes

第一个参数：InputArray类型的src，输入图像，需要是8位或者浮点型单通道、三通道的图像。
第二个参数：OutputArray类型的dst，需要与输入图像有一样的尺寸和类型。
第三个参数：int类型的d，表示在滤波过程中每个像素邻域的直径。如果这个值设为非正数，则从第五个参数sigmaSpace来计算它。
第四个参数：double类型的sigmaColor，颜色空间滤波器的sigma值。这个值越大，表示该像素邻域内有越宽广的颜色被混合到一起，会产生较大的半相等颜色区域。
第五个参数：double类型的sigmaSpace，坐标空间中滤波器的sigma值，坐标空间的标准方差。它的值越大，则越远的像素会相互影响，从而使更大的区域中足够相似的颜色获取相同的颜色。当d>0时，d指定了邻域大小且与sigmaSpace无关。fouze，d正比于sigmaSpace。
第六个参数：int类型borderType。


均值迁移滤波

pyrMeanShiftFiltering(src, sp, sr, dst=None, maxLevel=None, termcrit=None):

    .   @paramsrc The source 8-bit, 3-channel image.
    .   @param dst The destination image of the same format and the same size as the source.
    .   @param sp The spatial window radius.
    .   @param sr The color window radius.
    .   @param maxLevel Maximum level of the pyramid for the segmentation.
    .   @param termcrit Termination criteria: when to stop meanshift iterations.

第一个参数src，输入图像，8位，三通道的彩色图像，并不要求必须是RGB格式，HSV、YUV等Opencv中的彩色图像格式均可；
第二个参数dst，输出图像，跟输入src有同样的大小和数据格式；
第三个参数sp，定义的漂移物理空间半径大小；
第四个参数sr，定义的漂移色彩空间半径大小；
第五个参数maxLevel，定义金字塔的最大层数；
第六个参数termcrit，定义的漂移迭代终止条件，可以设置为迭代次数满足终止，迭代目标与中心点偏差满足终止，或者两者的结合；





"""


# 边缘保留滤波
def bi_demo(image):
    dist = cv.bilateralFilter(image, 0, 40, 15)
    return dist


def shift_demo(image):  # 均值迁移
    dist = cv.pyrMeanShiftFiltering(image, 10, 50)
    return dist


src1 = cv.imread('E:home.jpg', 1)  # 读入彩色图片
dist1 = bi_demo(src1)
cv.imshow("dist1", dist1)

dist2 = shift_demo(dist1)
cv.imshow("src", src1)
cv.imshow("dist",dist2)
cv.waitKey(0)
