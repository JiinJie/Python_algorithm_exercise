# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 16:34
# @Author  : jinjie
# @File    : HJ45_名字的漂亮度.py

"""
给出一个字符串，该字符串仅由小写字母组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。

给出多个字符串，计算每个字符串最大可能的“漂亮度”。
本题含有多组数据。
"""

n = int(input())
while n:
    try:
        temp_dict = {}
        str_in = input()
        for i in str_in:
            if temp_dict.get(i):
                temp_dict[i] += 1
            else:
                temp_dict[i] = 1

        # temp_sort = sorted(temp_dict.items(),key=lambda x:x[1]),reverse=True
        res_list = []
        for key, value in temp_dict.items():
            res_list.append(value)

        res_list.sort(reverse=True)

        sum = 0
        j = 26
        for i in res_list:
            sum += int(i) * j
            j -= 1
            # print(i,j)
        print(sum)

        n = n - 1
    except:
        break