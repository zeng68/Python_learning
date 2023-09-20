import os
import shutil

file_dir0 = "C:\\Users\\Administrator\\Desktop\\school\\data3"  # 要提取文件的文件夹路径
save_dir0 = "C:\\Users\\Administrator\\Desktop\\label\\jpggggg"  # 目的文件夹的路径
suffix = ['jpg']  # 要提取的文件格式列表,也就是说想提取啥类型文件,把后缀加进列表


def filterfile(file_dir, save_dir, suffix):
    '''
    该函数实现从文件夹中根据文件后缀名提取文件，并存储在新的文件夹中
    file_dir指读的文件目录；save_dir为保存文件的目录
    suffix用于存放打算提取文件的后缀名的列表；
    '''
    if os.path.exists(save_dir):
        shutil.rmtree(save_dir)  # 如果已经存在该文件夹，移除
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)  # 如果不存在该文件夹，则创建，用于储存后续提取出来的文件
    filelist = []  # 存储要copy的文件全名列表
    for dirpath, dirnames, filenames in os.walk(file_dir):  # 根据路径执行树状的遍历，分别遍历根目录，根目录下的文件夹，文件夹下的文件 dirpath主路径
        for file in filenames:  # 遍历文件夹中的文件  filenames 文档名列表
            file_type = file.split('.')[-1]  # 对文件名根据.进行分隔，实现文件名，后缀名的分离   split()函数返回的是个字符串列表,file_type分离的文件类型
            if (file_type in suffix):  # 下面根据后缀名是否在列表中，提取文件   suffix文件后缀格式
                file_fullname = os.path.join(dirpath, file)  # 文件全名(主路径+文件名)
                filelist.append(file_fullname)  # 将符合要求的文件存放在列表中
    for file in filelist:
        shutil.copy(file, save_dir)  # 将列表中的文件复制到新的文件夹  这里的file经过前面的和主路径拼接已经是一个完整的路径了
        # save_dir   目的文件夹的路径


filterfile(file_dir0, save_dir0, suffix)  # 调用filterfile(, ,)   file_dir0  要提取文件的文件夹路径
# save_dir0  目的文件夹的路径
# suffix     要提取的文件格式列表,也就是说想提取啥类型文件,把后缀加进列表
