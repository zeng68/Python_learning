"""
__call__() 方法是一个特殊方法（也称为魔术方法），用于将对象作为函数调用。当你使用函数调用语法 obj() 调用一个对象时，
Python 会检查该对象是否定义了 __call__() 方法。如果定义了，则会调用该方法来执行相应的操作。
具体来说，__call__() 方法使得对象可以像函数一样被调用。你可以在类中定义 __call__() 方法，以便在使用对象作为函数调用时自定义对象的行为。
"""


class Adder:
    def __init__(self, num):
        self.num = num

    def __call__(self, x):
        return self.num + x


# 创建一个 Adder 对象
adder = Adder(5)

# 将对象作为函数调用
result = adder(10)
print(result)  # 输出: 15
