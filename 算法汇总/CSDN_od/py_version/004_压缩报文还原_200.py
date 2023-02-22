# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 21:48
# @Author  : jinjie
# @File    : 004_压缩报文还原_200.py

"""
题目
为了提升数据传输的效率，会对传输的报文进行压缩处理。
输入一个压缩后的报文，请返回它解压后的原始报文。
压缩规贝刂：n[str]，表示方括号内部的str正好重复n次。
氵主意n为正整数（0<n<=100）
str只包含小写英文字母，不考虑异常情况。
注：
1）原始报文长度不会超过1000，不考虑异常的情况
输入
输入压缩后的报文：
1，不考虑无效的输入，报文没有额外的空格，方括号总是符合格式要求的；
2，原始报文不包含数字，所有的数字只表示重复的次数n，例如不会出现像5b或3[8]的输入；
输出
解压后的原始报文
"""

# 方法一：辅助栈  参考-- 018_栈与队列_字符串解码

str_in = input()

stack,res,nums = [],"",0

for i in str_in:
    if i == "[":
        stack.append([res,nums])
        res,nums="",0
    elif i == "]":
        mult_res,last_num = stack.pop()
        res = mult_res + last_num*res
    elif '0'<= i <= '9':
        nums = nums*10 + int(i)
    else:
        res += i
print(res)


