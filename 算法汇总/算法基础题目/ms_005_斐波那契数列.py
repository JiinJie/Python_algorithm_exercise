# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 15:22
# @Author  : jinjie
# @File    : ms_005_斐波那契数列.py
# 数列满足规律：后一项等于前两项之和。如 1、1、2、3、5、8、13...

# 求满足规律的100以内的斐波那契数列


# 递归实现
a = 0
b = 1
L = []
while True:
    temp = a+b
    a = b
    if temp > 100:
        break
    else:
        b = temp
        L.append(b)
print(L)



# 参考答案
a = 0
b = 1
while b < 100:
    print(b, end=",")
    a, b = b, a+b


# 非递归实现

f1 = 1
f2 = 1
L2 = [f1,f2]
while True:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    if f3<100:
        L2.append(f3)
    else:
        break
print('\n')
print(L2)