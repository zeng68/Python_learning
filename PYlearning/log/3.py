import logging

# 输出格式和添加一些公共信息

logging.basicConfig(format="%(asctime)s|%(message)s", filename='demo.log', filemode='w', level=logging.DEBUG)
name = '张三'
age = 10
logging.debug("姓名 %s,年龄 %d", name, age)

