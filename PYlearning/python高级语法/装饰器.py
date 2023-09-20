'''
装饰器（一般情况下是输入一个函数，返回一个函数）
装饰器的作用：假如许多函数在执行前要进行一些相同的操作，如果把这些相同的操作全部都一个个
写入每个函数当中，这不免会发生代码的冗余。所以我们引入装饰器，我们希望经过装饰器装饰后，
函数能达到以前写成冗余代码时相同的效果。（在函数执行前把相同操作的操作执行一下）
比如如下的例子：每个人生下来的第一件事就是哭
这里定义一个cry装饰器函数（输入参数为person函数，返回的是person函数），如果
在定义person(name:str)函数之前加上 @cry 装饰器 那么每次调用person(name:str)
函数就会先进行cry装饰器装饰。具体过程如下：
首先执行person('Tom')
进入cry(person)函数，在返回healthy函数之前，先进行执行health()函数
打印 会哭
返回result(*args, **kwargs)函数，这个result(*args, **kwargs)也就是person()函数
最后像往常一样正常执行person('Tom)

这样做的好处就是我们没有动person()函数却能给person()函数增加一些功能，如果有其他函数也有像person()
函数 ’会哭‘ 的前处理操作，也不需要在其他函数内部重写这个’会哭‘语句，只需要在这个函数之前加上@cry装饰器就可以实现’会哭‘
语句，这大大减少了代码的冗余。增加了代码的逻辑性。

'''


def cry(person):
    def health(*args, **kwargs):
        print("会哭")
        result = person(*args, **kwargs)
        return result

    return health


@cry  # 装饰器要在被装饰的person函数之前
def person(name: str):
    print(name + "健康成长")


person('Tom')






# 例2
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def my_function():
    print("Inside function")
    print("123")

my_function()





"""
例二

在装饰器模式中，装饰器函数应该返回一个函数对象，它会替代原始函数的调用。这个函数对象就是包装器函数 wrapper。
当你在使用装饰器 @log_decorator 修饰函数 add 时，实际上是将 add 函数作为参数传递给了装饰器函数 log_decorator。
装饰器函数会对传入的函数进行装饰，并返回一个新的函数对象 wrapper。然后，新的函数对象会替代原始函数 add，在调用 add 时执行装饰器的逻辑。



def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        result = func(*args, **kwargs)
        print("Function result:", result)
        return result
    return wrapper


@log_decorator
def add(a, b):
    return a + b


# 调用被装饰的函数
result = add(3, 5)
# Output:
# Calling function: add
# Function result: 8


"""