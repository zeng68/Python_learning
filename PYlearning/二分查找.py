import bisect
import numpy as np
a = [1.0,2.0,5.0,5.0,5.0]
print(bisect.bisect_left(a, 4.9))#在a数组中二分查找待插入数据4.9的位置，并返回插入位置的数组下标，存在左插入和右插入

print(a[:-3:-1])

