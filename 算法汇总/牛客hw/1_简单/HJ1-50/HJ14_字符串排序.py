# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 14:42
# @Author  : jinjie
# @File    : HJ14_字符串排序.py

"""
给定 n 个字符串，请对 n 个字符串按照字典序排列。
"""

str_len = int(input())
temp_list = []

for i in range(str_len):
    temp_list.append(input())

temp_list.sort()
for i in range(str_len):
    print(temp_list[i])