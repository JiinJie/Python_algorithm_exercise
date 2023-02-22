# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 12:29
# @Author  : jinjie
# @File    : HJ100_等差数列.py
"""
等差数列 2，5，8，11，14。。。。
（从 2 开始的 3 为公差的等差数列）
输出求等差数列前n项和
"""

n = int(input())

sum = 2
num = 2
#temp_str = "2"
for i in range(n-1):
    num += 3
    #temp_str=temp_str+'+'+str(num)
    sum += num
print(sum)  #直接输出sum如：7
#print(f"{temp_str}={sum}")  #输出公式如：2+5=7