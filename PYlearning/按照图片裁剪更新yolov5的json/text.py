import json
import numpy as np
import cv2
import copy
import os
import shutil
import random
from tqdm import tqdm
import random

# root = r'C:\Users\gw_zengqg\Desktop\yoloresize\labeled_wsh_2023-4-28'
root = r'C:\Users\gw_zengqg\Desktop\resize'
# root = r'C:\Users\gw_zengqg\Desktop\121323123'
save_path1 = 'C:\\Users\\gw_zengqg\\Desktop\\pyyolo\\zqg_split_1024NNULL_new'
save_path2 = 'C:\\Users\\gw_zengqg\\Desktop\\pyyolo\\zqg_split_1024NNULL_new2'


def resize_img(img, data1):
    ############     resize图像到指定大小
    new_width = 830
    new_height = 1024
    old_height = img.shape[0]
    old_width = img.shape[1]
    img = cv2.resize(img, (new_width, new_height))
    # 更新矩形框坐标信息
    for points in data1['shapes']:
        x1 = points['points'][0][0]
        y1 = points['points'][0][1]
        x2 = points['points'][1][0]
        y2 = points['points'][1][1]

        # 根据 resize 操作的比例更新矩形框坐标
        x1 = int(x1 * (new_width / old_width))
        y1 = int(y1 * (new_height / old_height))
        x2 = int(x2 * (new_width / old_width))
        y2 = int(y2 * (new_height / old_height))

        # 更新矩形框坐标信息
        points['points'][0][0] = x1
        points['points'][0][1] = y1
        points['points'][1][0] = x2
        points['points'][1][1] = y2
    data1['imageHeight'] = new_height
    data1['imageWidth'] = new_width
    return img, data1


def crop_img(img, balck_edge):
    # 寻找最大矩形裁剪，并更新json
    image = img
    # 转换为灰度图像
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 使用二值化将图像转换为黑白图像
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # 查找轮廓
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 寻找最大轮廓
    largest_contour = max(contours, key=cv2.contourArea)
    # 获取最大轮廓的外接矩形
    x, y, w, h = cv2.boundingRect(largest_contour)
    # 裁剪出最大物体
    cropped_image = image[y:y + h, x - balck_edge:x + w]
    return cropped_image, x, y, w, h


def update_yolov5_json(json_path, x, y):
    # 读取JSON文件
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)

    # 更新points信息
    for obj in json_data['shapes']:
        if 'points' in obj:
            a = obj['points'][0][0] = obj['points'][0][0] - x
            b = obj['points'][0][1] = obj['points'][0][1] - y
            c = obj['points'][1][0] = obj['points'][1][0] - x
            d = obj['points'][1][1] = obj['points'][1][1] - y
        # 更新后的JSON文件
        return json_data


split_list = [0, 512, 1024, 1536, 2048, 2560, 3072]
for file_name in tqdm(os.listdir(root)):
    random_number = random.randint(0, 9)
    chick_i = 1000
    if random_number == 9:
        save_path = save_path1
    else:
        save_path = save_path2
    # file_name= '192726098549_045_1.json'
    if '.json' in file_name:
        mask_zeros = {}
        tmp_json = None
        with open(os.path.join(root, file_name), 'r') as f:
            data = json.load(f)
            for labels in data['shapes']:
                # for key,value in labels.items():
                mask_zeros[labels['label']] = np.zeros((4096, 2048), dtype=np.uint8)
                if int(labels['points'][0][1]) < int(labels['points'][1][1]):
                    mask_zeros[labels['label']][int(labels['points'][0][1]):int(labels['points'][1][1]),
                    int(labels['points'][0][0]):int(labels['points'][1][0])] = 100
                else:
                    mask_zeros[labels['label']][int(labels['points'][1][1]):int(labels['points'][0][1]),
                    int(labels['points'][1][0]):int(labels['points'][0][0])] = 100

        img = cv2.imread(os.path.join(root, file_name[:-4] + 'jpg'))
        if img.shape[0] < 2000:
            black_edge = 20  # 可调黑色背景边缘参数（距离图像左右边界）
            # 寻找最大矩形裁剪
            img, x, y, w, h = crop_img(img, black_edge)
            data1 = update_yolov5_json(os.path.join(root, file_name), x - black_edge, y)  # 对裁剪后的图更新其对应的json文件
            # resize图像到指定大小 并更新json
            img, data1 = resize_img(img, data1)
            # 将更新后的字典保存回 JSON 文件
            with open(os.path.join(save_path, file_name), 'w') as f:
                json.dump(data1, f)
            cv2.imwrite(os.path.join(save_path, file_name[:-5] + '.jpg'), img)
            continue

        for split_start in split_list:
            chick_i += 1
            tmp_shapes = []
            img_1 = img[split_start:split_start + 1024, 520:1350]
            tmp_json = copy.deepcopy(data)
            for key, value in mask_zeros.items():
                value_tmp = value[split_start:split_start + 1024, 520:1350]
                if np.sum(value_tmp) != 0:
                    # 使用findContours函数查找图像中的轮廓
                    contours, _ = cv2.findContours(value_tmp, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                    # 遍历所有轮廓，并找到每个轮廓的外接矩形
                    for cnt in contours:
                        x, y, w, h = cv2.boundingRect(cnt)
                        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        tmp_shapes.append({'label': key, 'points': [[x, y], [x + w, y + h]], 'group_id': None,
                                           'shape_type': 'rectangle', 'flags': {}})
            if np.sum(img_1 > 50) / img_1.shape[0] / img.shape[1] > 0.5 and len(tmp_shapes) > 0:
                cv2.imwrite(os.path.join(save_path, file_name[:-5] + str(chick_i) + '.jpg'), img_1)
                tmp_json['shapes'] = tmp_shapes
                tmp_json['imagePath'] = os.path.join(file_name[:-5] + str(chick_i) + '.jpg')
                tmp_json['imageHeight'] = img_1.shape[0]
                tmp_json['imageWidth'] = img_1.shape[1]
                tmp_json['imageData'] = None

                with open(os.path.join(save_path, file_name[:-5] + str(chick_i) + '.json'), 'w') as f:
                    json.dump(tmp_json, f)
    else:
        # if os.path.exists(os.path.join(root,file_name[:-3]+'json')):
        #     continue
        # img = cv2.imread(os.path.join(root,file_name))
        # if img.shape[0]>1000:

        #     for split_start in split_list:
        #         chick_i+=1
        #         tmp_shapes=[]

        #         img_1 = img[split_start:split_start+1024,:][:,500:1500]
        #         if np.sum(img_1!=0)/img_1.shape[0]/img.shape[1]>0.5:

        #             cv2.imwrite(os.path.join(save_path,file_name[:-5]+str(chick_i)+'.jpg'),img_1)
        # else:
        #     shutil.copy(os.path.join(root,file_name),os.path.join(save_path,file_name))
        #     print(file_name)
        pass
        # if os.path.exists(path)