# """
# *********************************************************************************************************
#             字典是一种映射类型，它的元素是键值对，字典的关键字必须为不可变类型，(元祖/字符串/数字),且不能重复。创建空字典使用{}。
#
#                             1. 创建字典的两种方式
#                                     1.1 直接使用 "{}"
#                                     1.2 使用dict()
#                             2.空字典
#
# """
# c = dict((["年龄", "18"], ["姓名", "ZQG"]))  # 把元素是列表的元祖转化为字典
# print(c)  # 打印:{'年龄': '18', '姓名': 'ZQG'}
#
# #   1. 空字典
# d = {}  # 直接写大括号表达的是字典,不是集合
#
# #   2. 空集合
# f = set()




''''
第一种用法：  字典键来访问字典中的值
loss = {'loss_seg': 0.123, 'acc_seg': 0.89}
loss_seg_value = loss['loss_seg']
acc_seg_value = loss['acc_seg']

print(loss_seg_value)  # 输出: 0.123
print(acc_seg_value)  # 输出: 0.89






第二种用法：get()方法来替代索引操作。get()方法允许我们指定一个默认值，在字典中找不到指定键时返回该默认值。
loss = {'loss_seg': 0.123, 'acc_seg': 0.89}
loss_seg_value = loss.get('loss_seg', 0)
acc_seg_value = loss.get('acc_seg', 0)
nonexistent_value = loss.get('nonexistent_key', 'Not Found')

print(loss_seg_value)  # 输出: 0.123
print(acc_seg_value)  # 输出: 0.89
print(nonexistent_value)  # 输出: Not Found





'''
