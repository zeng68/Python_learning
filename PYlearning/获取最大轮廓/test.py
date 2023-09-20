# -------------------------------------------------------------------------------------
import cv2


def find_largest_object(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 进行二值化处理
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # 查找轮廓
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大轮廓
    max_contour = max(contours, key=cv2.contourArea)

    # 获取最大轮廓的外接矩形
    x, y, w, h = cv2.boundingRect(max_contour)

    # 绘制外接矩形
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0),
                  2)  # cv2.boundingRect() 函数将计算给定轮廓的外接矩形框，并返回其左上角坐标 (x, y) 以及宽度 w 和高度 h。

    # 显示结果图像
    cv2.imshow("Largest Object", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 示例用法
if __name__ == '__main__':
    image_path = r"122.jpg"  # 替换为您的图像路径
    find_largest_object(image_path)

