# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 15:47
# @Author  : jinjie
# @File    : HJ22_汽水瓶.py
"""
某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。
数据范围：输入的正整数满足  1≤n≤100
注意：本题存在多组输入。输入的 0 表示输入结束，并不用输出结果。
"""

def max_bottles(n):
    result = n//3
    bottles = n//3 + n%3
    if bottles == 2:
        result += 1
    elif bottles<2:
        result += 0
    else:
        result += max_bottles(bottles)
    return result

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(max_bottles(n))