import logging

# 默认的日志输出级别为warning
print("this is a print log")
logging.basicConfig(filename='demo.log', filemode='w', level=logging.ERROR)
logging.debug("This is a debug log")
logging.info("This is info log")
logging.warning("This is warning log")
logging.error("This is error log")
logging.critical("This is critical log")
