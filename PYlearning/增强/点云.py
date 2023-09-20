from plyfile import PlyData, PlyElement
import numpy as np
import pandas as pd
import cv2
from PIL import Image
import os

def plyZ2img(ply_data):
    ply_data = ply_data * -1
    max_num = np.max(ply_data)
    min_num = np.min(ply_data)
    ply_data[ply_data == 0.0] = min_num
    if min_num == 0.0:
        ply_data = ply_data + 1
        min_num = 1.0
        max_num = max_num + 1.0

    ply_data = (ply_data - min_num) / (max_num - min_num) * 10
    ply_data = ply_data.astype(np.uint8)
    return ply_data




# 根目录
root_dir = r'D:\cloud_points\all_data'

# 遍历目录结构
for __, date_dirs, _ in os.walk(root_dir):
    # if not date_dir.startswith('/path/to/root/dir/date_'):
    #     continue
    for date_dir in date_dirs:

        # 遍历编号文件夹
        for _, id_dirs, files in os.walk(os.path.join(root_dir, date_dir)):
            # if not id_dir.startswith('/path/to/root/dir/date_/id_'):
            #     continue

            # 遍历所有图像并读取
            # try:
            for filename in files:
                if filename.endswith('.jpg'):
                    # print(date_dir)
                    # print(id_dirs)
                    # print(_)

                    # print(files)
                    # for id_idr in id_dirs
                    try:
                        img_path = os.path.join(_, filename)
                        with Image.open(img_path) as img:
                            # 处理图像
                            img = np.array(img)
                            # if 'jpg' in name:
                            #          img_file = os.path.join(root,name)
                            ply_file = img_path[:-3] + 'ply'

                            # img = cv2.imread(os.path.join(root,name),0)
                            w, h = img.shape
                            plydata = PlyData.read(ply_file)  # 读取文件
                            data = plydata.elements[0].data  # 读取数据
                            data_pd = pd.DataFrame(data)  # 转换成DataFrame, 因为DataFrame可以解析结构化的数据
                            data_np = np.zeros(data_pd.shape, dtype=np.float16)  # 初始化储存数据的array
                            property_names = data[0].dtype.names  # 读取property的名字
                            for i, name_ in enumerate(property_names):  # 按property读取数据，这样可以保证读出的数据是同样的数据类型。
                                data_np[:, i] = data_pd[name_]
                            ply_img = plyZ2img(data_np[:, 2]).reshape(w, h)
                            img_merge = cv2.merge([img, ply_img, ply_img])
                            # ply_img = ply_img.reshape(w,h)
                            img_array = Image.fromarray(img_merge)
                            img_array.save(img_path[:-4] + '.png')
                            # cv2.imwrite(img_path[:-4]+'1.png',img_merge)
                            print(img_path)
                    except:
                        pass