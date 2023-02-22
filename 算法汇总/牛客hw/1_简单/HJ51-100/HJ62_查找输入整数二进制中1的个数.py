# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 16:29
# @Author  : jinjie
# @File    : HJ62_查找输入整数二进制中1的个数.py

"""
输入一个正整数，计算它在二进制下的1的个数。
注意多组输入输出！！！！！！

数据范围： 1≤ n ≤2^31−1
"""

while True:
    try:
        num_in = int(input())
        sum = 0
        # 将字符串前缀的进制符号去除
        num_bin = bin(int(num_in))[2:]
        for i in num_bin:
            if i == '1':
                sum += 1

        print(sum)
    except:
        break