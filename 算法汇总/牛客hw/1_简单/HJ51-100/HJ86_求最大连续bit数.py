# -*- coding: utf-8 -*-
# @Time    : 2023/2/10 11:51
# @Author  : jinjie
# @File    : HJ86_求最大连续bit数.py

"""
求一个int类型数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1
数据范围：数据组数：1≤t≤5 ，1≤n≤500000
进阶：时间复杂度：O(logn) ，空间复杂度：O(1)
"""


str_bin = bin(int(input()))[2:]
str_bin = str_bin.split('0')
res = 0
temp_count = 0

for i in str_bin:
    temp_count = i.count("1")
    if temp_count > res:
        res = temp_count
print(res)

