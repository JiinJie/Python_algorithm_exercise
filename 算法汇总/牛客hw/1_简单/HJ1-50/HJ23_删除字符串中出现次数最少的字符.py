# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 17:19
# @Author  : jinjie
# @File    : HJ23_删除字符串中出现次数最少的字符.py

"""
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，
则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
"""
str_in = input()
temp_dict = {}
res = ''

for i in str_in:
    if temp_dict.get(i):
        temp_dict[i] += 1
    else:
        temp_dict[i] = 1
# 按value的值从小到达排序字典
# order_dict = dict(sorted(temp_dict.items(), key=lambda x: x[1]))
min_value = min(temp_dict.values())
for i in str_in:
    if temp_dict[i] != min_value:
        res += i
print(res)
