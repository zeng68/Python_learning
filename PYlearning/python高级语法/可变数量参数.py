def example_func(*args, **kwargs):
    print(args)  # 打印位置参数（元组）
    print(kwargs)  # 打印关键字参数（字典）


# 调用示例函数
example_func(1, 2, 3, a='apple', b='banana')
