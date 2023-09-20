import logging

# 向日志输出变量
name = '张三'
age = 10
logging.basicConfig(filename='demo.log', filemode='w', level=logging.DEBUG)
logging.debug("姓名 %s,年龄 %d", name, age)
logging.debug("姓名 %s,年龄 %d" % (name, age))
logging.debug("姓名{},年龄 {}".format(name, age))
logging.debug(f"姓名 {name},年龄 {age}")


