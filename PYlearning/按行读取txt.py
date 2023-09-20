"""
需要注意的是，strip()方法只会去除字符串首尾的指定字符，不会去除字符串中间的字符。
如果想要去除字符串中的指定字符，可以使用replace()方法或正则表达式等方法。

string.replace(old, new[, count])
其中，string是需要进行替换操作的字符串，old是要被替换的子串，new是替换后的子串，
count是可选参数，用于指定最多替换多少个子串。如果不指定count参数，则默认替换所有的子串。
replace()方法不会修改原始的字符串，而是返回一个新的字符串


"""

filename = r"C:\Users\Administrator\Desktop\PYlearning\log\demo.log"
content_list = []

with open(filename, "r") as file:
    for line in file:
        # content_list.append(line.strip())
        content_list.append(line)

print(content_list)
