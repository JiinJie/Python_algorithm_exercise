# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 17:21
# @Author  : jinjie
# @File    : HJ20_补充_公共子串.py

# """
# -----------------------------------------
# # 长度为4的公共字串肯定包含长度为3的多个公共字串，
# #因此直接计算字符串中是否包含长度为3的子字符串即可
# -----------------------------------------
# """

# 方法一：直接遍历寻找
#str_in = input()
str_in = '021Abc9Abc1'

# for i in range(len(str_in) - 3):
#     temp_str = str_in[i:i + 3]
#     new_len = str_in.split(temp_str)
#     if len(new_len) >= 3:  #判断字符串是否有重复子串
#         print("有重复的公共子串")

# 方法二：使用count判断子串出现的次数
for i in range(len(str_in)-3):
    temp_str = str_in[i:i+3]
    res = str_in.count(temp_str)

    if res > 1:
        print("有重复的公共子串")