# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 14:01
# @Author  : jinjie
# @File    : HJ55_挑7.py

"""
输出 1到n之间 的与 7 有关数字的个数。
一个数与7有关是指这个数是 7 的倍数，或者是包含 7 的数字（如 17 ，27 ，37 ... 70 ，71 ，72 ，73...）
"""


str_in = int(input())
res = 0


for i in range(str_in+1):
    if ("7" in str(i) or i%7 == 0)and i!=7:
        #print(i)
        res += 1

print(res)