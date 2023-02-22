# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 16:02
# @Author  : jinjie
# @File    : ms_007_汉诺塔.py

# 汉诺塔  n表示几个盘子 a,b,c分别表示三个柱子

def hanoi(n,a,b,c):
    if n == 1:
        print(a,'-->',c)

    else:
        hanoi(n-1,a,c,b)
        print(a,'-->',c)
        hanoi(n-1,b,a,c)

hanoi(5,'A','B','C')


