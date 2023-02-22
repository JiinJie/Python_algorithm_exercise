# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 13:50
# @Author  : jinjie
# @File    : HJ108_★求最小公倍数.py

"""
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。
"""
"""
输出描述：
输出A和B的最小公倍数。

示例1
输入：5 7
输出：35
"""

a,b = list(map(int,input().split()))
if a <= b:
    a,b = b,a
    for i in range(a,a*b+1,a): # 步长为a进行循环遍历保证可以被a整除
        if i%b == 0:
            print(i)
            break
