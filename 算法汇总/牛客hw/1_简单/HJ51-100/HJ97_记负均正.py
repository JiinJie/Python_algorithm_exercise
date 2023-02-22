# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 11:56
# @Author  : jinjie
# @File    : HJ97_记负均正.py

"""
首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。
0即不是正整数，也不是负数，不计入计算。如果没有正数，则平均值为0。
"""
str_num = input()
str_in = list(input().split())

fu_time = 0
zheng_time = 0
res = 0
for i in str_in:
    if i == '0':
        pass
    elif int(i) > 0:
        res += int(i)
        zheng_time +=1
    else:
        fu_time += 1

if zheng_time == 0:
    print(fu_time,'0.0')
else:
    print(fu_time,"%.1f" %(res/zheng_time))  #格式化输出，保留一位小数
