# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 22:46
# @Author  : jinjie
# @File    : HJ4_字符串分割.py


str = input()

def add_zero(str):
    zero = len(str)%8
    for i in range(8-zero):
        str += '0'

    return str


str = add_zero(str)
x = len(str)//8
for i in range(x):
    print(str[i*8:(i+1)*8])


