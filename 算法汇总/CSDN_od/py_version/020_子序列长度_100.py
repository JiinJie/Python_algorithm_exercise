# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 13:48
# @Author  : jinjie
# @File    : 020_子序列长度_100.py

"""
机试题目
有N个正整数组成的一个序列
给定一个整数sum
求长度最长的的连续子序列使他们的和等于sum
返回次子序列的长度
如果没有满足要求的序列返回 -1
"""

str_in = list(input().split(","))
sums = int(input())
res = []

for i in range(len(str_in)):
    temp_list = []
    for j in range(i,len(str_in)):
        temp_list.append(int(str_in[j]))
        if sum(temp_list) == sums:
            res.extend([temp_list])
            break
#print(res)

max_len = -1
for i in res:
    if len(i)>max_len:
        max_len = len(i)

print(max_len)
