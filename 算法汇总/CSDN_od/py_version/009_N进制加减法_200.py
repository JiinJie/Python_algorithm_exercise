# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:21
# @Author  : jinjie
# @File    : 009_N进制加减法_200.py

"""
N进制减法
题目
实现一个基于字符串的N进制减法。
需要对输入的两个字符串按照给定的N进制进行减法操作，输出正负符号和表示结果的字符串
输入
三个参数。
第一个参数是整数形式的进制N值，2<=N<=35，
第二个参数为被减数字符串；
第三个参数为减数字符串。
有效的字符包括0、9以及小写字母a--z，字符串有效字亻寸个数最大为100个字符，另外还有结尾的\0。
·限制：
输入的被减数和整数，除了单独的0以外，不能是以0开头的字符串。
如果输入有异常或者计算过程中有异常此时应当输出·1表示错误。
"""




def transform(n, m):  # n为待转换的十进制数，m为要转换成的进制数
    str_ = ''
    trans = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n']  # 列表trans中的元素个数与转换后的进制数相同
    remainder = []  # 用于储存余数
    while n > 0:
        x = n % m
        remainder.append(x)
        n = n // m
    remainder.reverse()  # 模拟手算进制转换时的倒写
    for item in remainder:
        str_ += str(trans[item])
    return str_


str_in = input().split()
n, num1, num2 = int(str_in[0]), str_in[1], str_in[2]

cacul = int(num1, n) - int(num2, n)

print(transform(cacul, n))