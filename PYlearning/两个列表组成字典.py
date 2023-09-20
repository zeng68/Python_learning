# 三种方式将两个列表组成字典
list1 = ['张三', '李四', '王五']
list2 = [80, 85, 90]

# 1. 使用 for 循环
result = {}
for key, value in zip(list1, list2):
    result[key] = value
print(result)

# 2. 使用字典生成式
result = {key: value for key, value in zip(list1, list2)}
print(result)

# 3.使用dist函数


result = dict(zip(list1, list2))
print(result)
