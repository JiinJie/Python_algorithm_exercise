# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 11:14
# @Author  : jinjie
# @File    : HJ52_计算字符串的编辑距离.py

"""
Levenshtein 距离，又称编辑距离，指的是两个字符串之间，由一个转换成另一个所需的最少编辑操作次数。许可的编辑操作包括将一个字符替换成另一个字符，插入一个字符，删除一个字符。编辑距离的算法是首先由俄国科学家 Levenshtein 提出的，故又叫 Levenshtein Distance 。
例如：
字符串A: abcdefg
字符串B: abcdef
通过增加或是删掉字符 ”g” 的方式达到目的。这两种方案都需要一次操作。把这个操作所需要的次数定义为两个字符串的距离。
要求：
给定任意两个字符串，写出一个算法计算它们的编辑距离。
"""

str_org = input()
str_trs = input()

m = len(str_org)
n = len(str_trs)

# 创建 dp二维数组
dp = [[x for x in range(n+1)] for y in range(m+1)]

for i in range(n+1):
    dp[0][i] = i  #若对比字符为空，最多需要len(str_trs)次
for j in range(m+1):
    dp[j][0] = j  #若对比字符为空，最多需要len(str_org)次

for i in range(1,m+1):
    for j in range(1,n+1):
        if str_org[i-1] == str_trs[j-1]:  #如果相等即不需要操作，使用上一个参数值
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1   #取最小值，然后+1

print(dp[m][n])