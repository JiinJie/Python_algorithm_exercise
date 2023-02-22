# -*- coding: utf-8 -*-
# @Time    : 2023/2/10 11:25
# @Author  : jinjie
# @File    : HJ84_统计大写字母个数.py

"""
找出给定字符串中大写字符(即'A'-'Z')的个数。
数据范围：字符串长度：1≤∣s∣≤250
字符串中可能包含空格或其他字符
进阶：时间复杂度：O(n) ，空间复杂度：O(n)
"""

str_in  = input()
res = 0
for i in str_in:
    if i.isupper():
        res +=1
print(res)