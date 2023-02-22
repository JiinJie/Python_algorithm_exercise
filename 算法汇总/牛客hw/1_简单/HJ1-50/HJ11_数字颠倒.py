# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 14:35
# @Author  : jinjie
# @File    : HJ11_数字颠倒.py

"""
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001
"""


num = input()
list_num = list(num)
str = ''

for i in range(len(list_num)):
    str += (list_num.pop())

print(str)