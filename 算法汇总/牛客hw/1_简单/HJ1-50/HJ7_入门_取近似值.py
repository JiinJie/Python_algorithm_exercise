# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 11:09
# @Author  : jinjie
# @File    : HJ7_入门_取近似值.py

"""
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。
如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。
"""

input_double = float(input())

num = int(input_double)
if (input_double - float(num))>=0.5:
    print(num+1)
else:
    print(num)