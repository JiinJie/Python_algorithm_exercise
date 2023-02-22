# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 14:52
# @Author  : jinjie
# @File    : HJ15_求int型正整数在内存中存储时1的个数.py
"""
输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
"""

num = int(input())
count = 0

list_str = list(bin(int(num)))  #转化为二进制

for i in range(len(list_str)):
    if  list_str[i] == '1':
        count += 1

print(count)