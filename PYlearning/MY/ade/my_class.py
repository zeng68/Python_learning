class person:
    hair = 'black'

    def __init__(self, name='li', age=18, hair='black'):
        self.hair = hair
        self.name = name
        self.age = age

    def say(self) -> int:
        print('我的名字是{}我{:.2f}岁了我的头发是{}颜色'.format(self.name, self.age, self.hair))
        return 0


def fly():
    print("人不会飞")
