# class Registry:
#     def __init__(self):
#         self.registry = {}
#
#     def register(self, key, value):
#         self.registry[key] = value
#
#     def get(self, key):
#         return self.registry.get(key)
#
#
# LOSSES = Registry()
#
#
# def mean_squared_error(x, y):
#     # 损失函数的实现
#     print(x + y)
#
#
# def cross_entropy_loss(x, y):
#     # 损失函数的实现
#     print(x - y)
#
#
# # 注册损失函数到LOSSES注册器
# LOSSES.register('mse', mean_squared_error)
# LOSSES.register('cross_entropy', cross_entropy_loss)
#
# # 获取已注册的函数
# mse_loss_func = LOSSES.get('mse')
# cross_entropy_loss_func = LOSSES.get('cross_entropy')
#
# # 使用从注册器获取的函数
# mse_loss_func(1, 1)
# cross_entropy_loss_func(1, 1)









# class Registry:
#     def __init__(self):
#         self.registry = {}
#
#     def register(self, key, value):
#         setattr(self, key, value)
#
#     def __getattr__(self, key):
#         return self.registry.get(key)
#
#
# LOSSES = Registry()
#
#
# def mean_squared_error(x, y):
#     # 损失函数的实现
#     print(x + y)
#
#
# def cross_entropy_loss(x, y):
#     # 损失函数的实现
#     print(x - y)
#
#
# # 注册损失函数到LOSSES注册器
# LOSSES.register('mse', mean_squared_error)
# LOSSES.register('cross_entropy', cross_entropy_loss)
#
# # 直接访问已注册的函数
# mse_loss_func = LOSSES.mse
# cross_entropy_loss_func = LOSSES.cross_entropy
#
#
# # 使用从注册器获取的函数
# mse_loss_func(1, 1)
# cross_entropy_loss_func(1, 1)







class Registry:
    def __init__(self):
        self.registry = {}

    def __call__(self, key):
        return self.registry.get(key)

    def register(self, key, value):
        self.registry[key] = value


LOSSES = Registry()


def mean_squared_error(x, y):
    # 损失函数的实现
    print(x + y)


def cross_entropy_loss(x, y):
    # 损失函数的实现
    print(x - y)


# 注册损失函数到LOSSES注册器
LOSSES.register('mse', mean_squared_error)
LOSSES.register('cross_entropy', cross_entropy_loss)

# 使用LOSSES对象直接获取已注册的函数
mse_loss_func = LOSSES('mse')
cross_entropy_loss_func = LOSSES('cross_entropy')

# 调用获取到的函数
mse_loss_func(1, 1)
cross_entropy_loss_func(1, 1)

