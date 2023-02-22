# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 22:24
# @Author  : jinjie
# @File    : HJ2_计算某字符出现次数.py

"""
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，
然后输出输入字符串中该字符的出现次数。（不区分大小写字母）
"""


import re

input_str = 'ABCabc'
char = 'A'
temp_list = list(input_str)

print(temp_list)

char_d = char.upper()
char_s = char.lower()


def get_num():
    num:int = 0
    for i in temp_list:
        #if re.findall(r'[A-Za-z]',char):
        if char.isascii():
            if i == char_d or i == char_s:
                num += 1
        elif i == char:
            num += 1
        else:
            return None
    return num


print(get_num())