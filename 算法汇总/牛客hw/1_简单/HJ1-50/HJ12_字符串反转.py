# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 14:36
# @Author  : jinjie
# @File    : HJ12_字符串反转.py

"""
接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
"""

temp_list = list(input())
str = ''

for i in range(len(temp_list)):
    str += temp_list.pop()

print(str)