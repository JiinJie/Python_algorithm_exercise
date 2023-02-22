# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 16:02
# @Author  : jinjie
# @File    : HJ54_表达式求值.py
"""
给定一个字符串描述的算术表达式，计算出结果值。
输入字符串长度不超过 100 ，合法的字符包括 ”+, -, *, /, (, )” ， ”0-9” 。
数据范围：运算过程中和最终结果均满足 ∣val∣≤2^31−1  ，即只进行整型运算，确保输入的表达式合法
"""

while True:
    try:
        str_in = input()
        # inpt = inpt.replace('[','(')
        # inpt = inpt.replace(']',')')
        # inpt = inpt.replace('{','(')
        # inpt = inpt.replace('}',')')
        print(int(eval(str_in)))
    except:
        break