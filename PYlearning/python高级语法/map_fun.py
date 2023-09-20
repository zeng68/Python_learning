def fun(n):
    return 2 * n


L = [1, 2, 3, 4, 5]
result = map(fun, L)  # 第一个参数为一个函数名 第二个参数为一个可迭代对象
print(result)# map()函数返回一个map类型的结果，这里转化为列表类型
print(list(result))# map()函数返回一个map类型的结果，这里转化为列表类型
