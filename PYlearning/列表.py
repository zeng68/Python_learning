"""
列表加法与乘法
"""
list1 = [1,2,3,4,"我爱你",[33,44,55]]#列表
print(len(list1))#列表长度

list2 = [10,20,30]
list3 =[1,2,3]
print(list2+list3)#列表加法
print(list2*3)#列表乘法
print("我爱你"*3)#字符串乘法

"""
列表的切片取值
"""
list4 = [10,20,30,40,50,60,70]
print(list4[0:3])#列表切片取左不取右
print(list4[-3:-1])#列表切片取左不取右
print(list4[-3:])#可以取到最后一个列表元素[50, 60, 70]
print(list4[:])#输出整个列表[10, 20, 30, 40, 50, 60, 70]
print(list4[1:6:2])#跨两步长取值[20, 40, 60]
print(list4[-6:-1:2])#[20, 40, 60]
print(list4[::-1])#列表反向




"""
  del方法 与 append方法
"""
a = [1,2,3]
#del a     #a变量对应内存已经被销毁
print(a)
a.append(4)
print(a)

"""
列表的操作方法
            1.insert 方发
              insert函数用于向列表中插入元素
              insert的第一个参数是插入的位置,第二个参数是要插入的对象,如下
              
            2.clear函数用于将列表清空

"""
list5 = [20,30,40,50]
list5.insert(2,[1,2,3])
print(list5)
list5.clear()#清空列表

"""     列表操作方法:
                1.remove函数:从列表中移除元素(重复的话移出列表中出现的第一个)
                2.pop函数用于移列表中指定位置的元素,并返回要移除的元素
                  在默认情况下,移出列表中最后一个元素
"""
list6 = ["hello","world","python","hello"]
#list6.remove("hello")#移除列表里第一个匹配的hello
print(list6)
a=list6.pop(3)#移除指定位置的列表元素
print(list6)
print(a)#pop返回的值


"""
            1. index(a,b,c) 第一个参数:待查找的对象  第二个参数:查找的起始范围  第三个参数:查找的结束范围   
                返回寻找到得列表元素下标
            2.  reverse()列表逆向排序
              
"""
list7 = ["hello", "world", "hello", "python"]
r = list7.index('hello')#默认范返回匹配到的第一个元素下标
print(r)
r2 = list7.index("hello",1,3)#取左不取右
print(r2)
list7.reverse()#或者 list7[::-1]但此操作并未真正改变list7列表的元素排序
print(list7)





"""             
                      列表操作方法      1.extend方法      
                                               在列表的末尾增加一个列表
                                               与append 相比 extend 可以一次增加多个元素
                                               注意:注意:〔使用extend函数和列表加法的结果
                                               是一样的，但是extend函数会将另一个列表并入当前列表，
                                               而列表加法是返回新的列表，为节约内存空间，更推荐使用extend函数来实现大列表的连接操作。)

"""
list8 = [1,2,3,4]
list8.extend([5,6,7])
print(list8)


list9 = [1,2,3]
list01=list9.copy()#深复制
del list9[0]
print(list01)

list10 = [11,12,13]
list02 = list10    #浅复制
del list10[1]
print(list02)


"""
     list sort()函数    排序函数
"""
list11 = [10,4,5,7,2,9,3]
list11.sort()#升序
list11.sort(reverse=True)#降序
print(list11)


"""

list.count()

"""
list12 = ["hello","hello","str","str","str","www","rrr"]
r=list12.count("str")
print(r)
