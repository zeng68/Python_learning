'''
匿名函数 lambda
 使用场景:
         1.任意多个参数和一个返回值的函数，我们可以定义为lambda函数
         2.lambda作为一个参数传递
'''
# 1.
sum_lambda = lambda x,y:x+y   # 定义lambda函数
print(sum_lambda(1,2))

# 2.
def fun(a,b,add): #add 是一个函数
    print(add(a,b))

fun(100,1,lambda a,b:a-b) #这里把定义的lambda函数传给add函数,add函数形式就是我们传入的lambda函数的定义形式


