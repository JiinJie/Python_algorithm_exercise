# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 12:38
# @Author  : jinjie
# @File    : HJ102★字符统计.py

"""
输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，
如果统计的个数相同，则按照ASCII码由小到大排序输出。
数据范围：字符串长度满足1≤len(str)≤1000
"""

str_in = input()

s = sorted(set(str_in))
# print(s) 此时s已经去重，作为key
ss = sorted(s,key=lambda x:str_in.count(x),reverse=True)  #排序的key为str_in出现的次数

print(''.join(ss))