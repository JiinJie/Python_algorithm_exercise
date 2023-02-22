# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 12:11
# @Author  : jinjie
# @File    : HJ99_自守数.py
"""
自守数是指一个数的平方的尾数等于该数自身的自然数。
例如：25^2 = 625，76^2 = 5776，9376^2 = 87909376。请求出n(包括n)以内的自守数的个数
"""

str_in = int(input())

res = 0
for i in range(str_in+1):
    i_len = len(str(i))
    #print(f"{i}*{i}={i*i}",(i*i)%(i_len*10))
    if (i*i)%(10**(i_len)) == i:
        #print(f"----{i}")
        res +=1
print(res)