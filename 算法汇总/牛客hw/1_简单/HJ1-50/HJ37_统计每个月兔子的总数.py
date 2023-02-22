# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 9:46
# @Author  : jinjie
# @File    : HJ37_统计每个月兔子的总数.py
"""
有一种兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子。
例子：假设一只兔子第3个月出生，那么它第5个月开始会每个月生一只兔子。
一月的时候有一只兔子，假如兔子都不死，问第n个月的兔子总数为多少？

数据范围：输入满足 1≤n≤31
"""
# 方法一:公式法（递归） （斐波那契数列）
while True:
    try:
        month=int(input())
        n=month-1
        def func(n):
            if n<2:#基线条件
                return 1
            else:#递归条件
                return func(n-1)+func(n-2)
        print(func(n))
    except:
        break


# 方法二:状态法
n = int(input())
k3 = 0
k2 = 0
k1 = 0

for i in range(n):
    k3 = k3 + k2
    k2 = k1
    if k3==0 and k2 == 0:
        k1 = 1
    elif k3==0 and k2 == 1:
        k1 = 0
    else:
        k1 = k3

print(k1+k2+k3)