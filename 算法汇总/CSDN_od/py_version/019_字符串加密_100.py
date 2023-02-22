# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 13:24
# @Author  : jinjie
# @File    : 019_字符串加密_100.py

"""
机试题目
给你一串未加密的字符串str，
讨对字符串的每一个字母进行改变来实现加密，
加密方式是在每一个字母str[i]偏移特定数组元素a[i]的量，
数组a前三位已经赋值：a[0]=1，a[1]=2，a[2]=4。
当i>=3时，数组元素a[i]=a[i-1]+a[i-2]+a[i-3]，
例如：原文abcde加密后bdgkr，其中偏移量分别是1，2，4，7，13。
"""

nums = int(input())

while nums:
    res = ""
    a = [1,2,4]
    str_in = input()
    for i in range(len(str_in)):
        if i <=2:
            res += chr((ord(str_in[i])-97+a[i])%26+97)
        elif i>2:
            a.append(a[i-1]+a[i-2] +a[i-3])
            res += chr((ord(str_in[i]) - 97 + a[i])%26+97)

    print(res)
    nums -= 1

