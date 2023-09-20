
"""
     str = "abcdefg.aaa.bbb.ccc.eee"
     str.split('.')      以 . 分割字符串  返回一个分割后的字符串列表
     print(str.split('.',2))   以 .分割字符串 从左到右分割两次    打印:['abcdefg', 'aaa', 'bbb.ccc.eee']
     print(str[:-4])                                         打印:  abcdefg.aaa.bbb.ccc
"""


str = "abcdefg.aaa.bbb.ccc.eee"
print(str.split('.')[-1])
print(str.split('.',2))
print(str[:-4])