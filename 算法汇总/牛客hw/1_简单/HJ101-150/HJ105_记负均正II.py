# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 13:47
# @Author  : jinjie
# @File    : HJ105_记负均正II.py


"""
输入 n 个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
本题有多组输入数据，输入到文件末尾。

输入描述：
输入任意个整数，每行输入一个。
输出描述：
输出负数个数以及所有非负数的平均值
"""


fu_time = 0
zheng_time = 0
sum = 0
while True:
    try:
        str_in = int(input())
        if str_in >=0:
            zheng_time += 1
            sum += str_in
        else:
            fu_time += 1
    except:
        break

print(fu_time)
if zheng_time ==0:
    print('0.0')
else:
    res = "%.1f" %(sum/zheng_time)
    print(res)