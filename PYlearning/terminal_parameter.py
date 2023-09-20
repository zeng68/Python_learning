import argparse

'''
argparse是python用于解析命令行参数的标准模块。
我们很多时候，需要用到解析命令行参数的程序，例如在终端窗口输入(深度学习)训练的参数和选项。
参考：https://zhuanlan.zhihu.com/p/548773312
'''
parser = argparse.ArgumentParser(description='姓名')  # 创建一个解析对象
parser.add_argument('--family', type=str, help='姓')  # 添加命令行参数
parser.add_argument('--name', type=str, help='名')
parser.add_argument('--age', type=int, default='30', required=False, help='年龄')
args = parser.parse_args()  # 解析参数

# 打印姓名
STR = args.age
print(args.family + args.name)
