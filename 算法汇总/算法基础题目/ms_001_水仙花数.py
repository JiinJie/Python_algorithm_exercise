# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 14:15
# @Author  : jinjie
# @File    : ms_001_水仙花数.py
# 打印100-999之间所有的水仙花数，三位的立方和等于本身。如153 = 1^3+5^3+3^3

list_a = []
for a in range(100,1000):
    i = int(a/100)
    j = int(a/10)%10
    k = a%10
    if a == i**3+j**3+k**3:  # python中n方为a**n如：3次方为 a**3
        list_a.append(a)


print(list_a)
