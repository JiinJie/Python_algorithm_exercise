# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 15:13
# @Author  : jinjie
# @File    : ms_004_计算阶乘.py
# 计算 n 的阶乘,n! 例如： n=3时，阶乘为 3*2*1=6

# 求10的阶乘 10！


# 方法一 reduce
from functools import reduce
a = 10
b = reduce(lambda x,y:x*y,range(1,a+1))
print(b)


# 方法二 for写循环【不推荐】
a = 10
b = 1
for i in range(1,a+1):
    b = b*i
print(b)


# 方法三 递归实现
from functools import reduce

def chengfa(x, y):
    return x*y
a = 10
b = reduce(chengfa, range(1, a+1))
print(b)


