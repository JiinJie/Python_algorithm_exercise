# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 15:10
# @Author  : jinjie
# @File    : HJ59_找出字符串中第一个只出现一次的字符.py


"""
找出字符串中第一个只出现一次的字符
"""
# 方法一：


# 方法二：使用hash表存储


str_in = input()

temp_dict = {}

for i in str_in:
    if temp_dict.get(i):
        temp_dict[i] += 1
    else:
        temp_dict[i] = 1

#print(temp_dict)

for i in range(len(str_in)):
    #print(str_in[i])
    if temp_dict[str_in[i]] == 1:
        print(str_in[i])
        break
    if i == len(str_in)-1:
        print(-1)
        break
