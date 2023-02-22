# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 16:53
# @Author  : jinjie
# @File    : HJ60_ 查找组成一个偶数最接近的两个素数.py
"""
任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对。
数据范围：输入的数据满足 4≤n≤1000
"""
from math import sqrt


def func_su_num(x):
    if x<= 2:
        return True
    else:
        for i in range(2,int(sqrt(x))+1):
            print(f"x和i的值为{x},{i}")
            if x%i == 0:
                return False
        # 循环结束，返回True
        return True


num = int(input())
for i in range(int(num/2),num):
    if func_su_num(i) and func_su_num(num-i):
        print(num-i,i)
        break

