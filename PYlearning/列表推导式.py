# 1.列表推导式
nums = [x for x in range(1, 11) if x % 2 == 0]
print(nums)

# 2.enumerate(iterable, start=0)
# 用于将一个可迭代对象转换为一个枚举对象，同时可以返回迭代次数和对应的元素值。
my_list = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(my_list):
    print(i, fruit)





