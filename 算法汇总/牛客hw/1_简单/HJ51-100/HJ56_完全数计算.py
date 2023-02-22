# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 16:32
# @Author  : jinjie
# @File    : HJ56_完全数计算.py
"""
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。

输入n，请输出n以内(含n)完全数的个数。

"""
num = int(input())

time_num = 0

for i in range(1,num):
    res = 0
    for j in range(1,i):
    #for j in range(1,int(sqrt(i))+1):
        if i%j == 0:
            #print(i,j,res)
            res += j
        else:
            pass
    if res == i:
        time_num +=1
print(time_num)

