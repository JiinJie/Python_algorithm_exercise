# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 10:28
# @Author  : jinjie
# @File    : HJ6_质数因子.py


"""
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
例 100 的质数
"""

import math

n = 60
#n = int(input())

for i in range(2, int(math.sqrt(n))+1):
    while n % i == 0:  # 能被整除一定是因子
        print(i, end=' ')
        n = n // i   # 获取n的子因子，然后再次寻找这个数的因子
if n > 2:
    print(n)
    
    
