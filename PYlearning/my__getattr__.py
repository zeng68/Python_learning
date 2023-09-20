# 开头以双下划线命名的为私有成员，只能被类自身调用

class A(object):
    __ID = 342201

    def __init__(self, hair, skin, ID):
        self.hair = hair
        self.skin = skin
        self.__ID = ID

    def country(self):
        print("China")

    def __getattr__(self, *args):  # 如果子类调用没有定义的属性，则会调用getattr()函数
        print("缺少相应属性函数")


person = A('black', 'yellow', '12334567')
# print(person.__ID)
person.country()
# print(person.hair)
