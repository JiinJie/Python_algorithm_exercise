# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 18:03
# @Author  : jinjie
# @File    : HJ65_查找两个字符串a,b中最长公共字串.py

"""
查找两个字符串a,b中的最长公共子串。若有多个，输出在较短串中最先出现的那个。
注：子串的定义：将一个字符串删去前缀和后缀（也可以不删）形成的字符串。请和“子序列”的概念分开！
"""

while True:
    try:
        a, b = input(), input()
        if len(a) > len(b):  # 如果a长则调换
            a, b = b, a

        res = ''
        for i in range(len(a)):  # 从短的字符串开始算
            for j in range(i + 1, len(a)):
                if a[i:j + 1] in b and j + 1 - i > len(res):
                    res = a[i:j + 1]
        print(res)


    except:
        break