# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 19:30
# @Author  : jinjie
# @File    : HJ26_字符串排序.py


"""
编写一个程序，将输入字符串中的字符按如下规则排序。

规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy

规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb

规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y
"""
"""
示例1
输入：A Famous Saying: Much Ado About Nothing (2012/8).
输出：A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).
"""


str_in = input()

temp_str = ""

for i in str_in:
    if i.isalpha():
        temp_str += i

temp_sort = sorted(temp_str,key=str.upper)

index = 0
res = ""

for i in str_in:
    if i.isalpha():
        res += temp_sort[index]
        index += 1
    else:
        res += i

print(res)
