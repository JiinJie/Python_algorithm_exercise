# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 14:47
# @Author  : jinjie
# @File    : ms_003_冒泡排序.py

# 实现冒泡排序，从小到大
a = [1, 3, 10, 9, 21, 35, 4, 6]
b = []
for i in range(1,len(a)):
    for j in range(1,len(a)-i):
        if(a[j]>a[j+1]):
            b = a[j]
            a[j] = a[j+1]
            a[j+1] = b

print(a)

# 使用pythn的sort函数
"""python list底层的sort排序算法采用了Timsort排序算法，
Timsort是结合了合并排序（merge sort）和插入排序（insert sort）而得出的排序算法。"""
c = a.sort()
print(c)

