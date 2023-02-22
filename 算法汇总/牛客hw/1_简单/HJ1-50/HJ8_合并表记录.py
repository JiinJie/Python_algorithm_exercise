# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 11:17
# @Author  : jinjie
# @File    : HJ8_合并表记录.py
"""
数据表记录包含表索引index和数值value（int范围的正整数），
请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照index值升序进行输出。
PS 要重新排序
"""

# 思路 将字典的key保存为列表，然后排序。再遍历读取key和value

temp_dict = {}
temp_list = []

input_len = int(input())
for i in range(input_len):
    get_key, get_value = input().split(' ')
    if temp_dict.get(get_key):
        temp_dict[get_key] += int(get_value)
    else:
        temp_dict[get_key] = int(get_value)
        temp_list.append(int(get_key))

temp_list.sort()
# print(temp_list)
# print(temp_dict)
for i in temp_list:
    print(i, temp_dict[f'{i}'])
