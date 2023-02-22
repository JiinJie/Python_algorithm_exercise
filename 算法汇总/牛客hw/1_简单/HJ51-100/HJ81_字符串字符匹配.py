# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 17:54
# @Author  : jinjie
# @File    : HJ81_字符串字符匹配.py

"""
判断短字符串S中的所有字符是否在长字符串T中全部出现。
请注意本题有多组样例输入。
数据范围: 1≤len(S),len(T)≤200
进阶：时间复杂度：O(n) ，空间复杂度：O(n)
"""

str_short = input()
str_long = input()

def judge_char():
    for i in str_short:
        if i not in str_long:
            return False
    return True


if judge_char():
    print("true")
else:
    print("false")