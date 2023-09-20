def fun(n) ->int:
    assert (n<=10) # 断言 assert 的作用是现计算表达式 expression ，如果其值为假（即为0），那么它先向 stderr 打印一条出错信息,然后通过调用 abort 来终止程序运行
    return n

if __name__ == '__main__':
   print(fun(10))