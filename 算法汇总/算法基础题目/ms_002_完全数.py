# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 14:22
# @Author  : jinjie
# @File    : ms_002_完全数.py

# 求1000以内的完全数。一个数恰好等于他的因子之和（不含本身），成为完全数。如 6 = 1+2+3

L = []
for i in range(1,1001):
    sum = 0
    for j in range (1,i):
        if (i%j==0):
            sum += j
    if sum == i:
        L.append(sum)

print(L)


