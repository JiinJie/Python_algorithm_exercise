# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 15:57
# @Author  : jinjie
# @File    : ms_006_幂的递归.py

# 幂的递归，计算x的n次方 x^n 如 3的4次方 3*3*3*3 =81

def mi(x,n):
    if n == 0:
        return 1
    else:
        return x*mi(x,n-1)


print(mi(3,4))