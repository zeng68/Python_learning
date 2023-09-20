import copy

# 创建一个包含列表的原始对象
original_list = [1, 2, [3, 4]]

# 浅拷贝
shallow_copy = original_list.copy()

# 深拷贝
deep_copy = copy.deepcopy(original_list)

# 修改原始对象的共享部分
original_list[2].append(5)

# 输出结果
print("Original List:", original_list)      # 输出: [1, 2, [3, 4, 5]]
print("Shallow Copy:", shallow_copy)        # 输出: [1, 2, [3, 4, 5]]
print("Deep Copy:", deep_copy)              # 输出: [1, 2, [3, 4]]

