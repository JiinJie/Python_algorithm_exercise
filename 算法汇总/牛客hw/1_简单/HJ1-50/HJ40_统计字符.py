# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 10:44
# @Author  : jinjie
# @File    : HJ40_统计字符.py

"""
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。
数据范围：输入的字符串长度满足  1≤n≤1000
"""

str_in = input()
num = [0,0,0,0]
for i in str_in:
    if i.isalpha():
        num[0] += 1
    elif i.isspace():
        num[1] += 1
    elif i.isalnum():
        num[2] += 1
    else:
        num[3] += 1

for i in range(len(num)) :
    print(f"{num[i]}")