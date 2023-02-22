# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 14:08
# @Author  : jinjie
# @File    : HJ57_高精度整数加法.py

"""
输入两个用字符串 str 表示的整数，求它们所表示的数之和。
"""

"""
示例1
输入：9876543210
1234567890
输出：11111111100
"""
#方法一：直接相加
#python语言支持大整数，不受位数限制

while True:
    try:
        n1 = int(input())
        n2 = int(input())
        print(n1+n2)		# 直接输出整型数字相加之和的结果
    except:
        break


# 方法二：逐位相加进位
str_1 = input()
str_2 = input()

if len(str_1) < len(str_2):  #长度不一致，进行补零
    str_1 = str_1.zfill(len(str_2))
else:
    str_2 = str_2.zfill(len(str_1))

str_1 = list(str_1)
str_2 = list(str_2)

j = 0
res = 0

for _ in range(len(str_1)):
    if len(str_2) != 0:
        sum_pop = (int(str_1.pop())+int(str_2.pop())) #从末尾开始相加
        res += sum_pop*10**j
        j +=1

print(res)