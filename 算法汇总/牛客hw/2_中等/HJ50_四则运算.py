# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 18:09
# @Author  : jinjie
# @File    : HJ50_四则运算.py

"""
输入一个表达式（用字符串表示），求这个表达式的值。
保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。
"""
# 方法一：直接使用eval
str_in = input().replace('[', '(').replace(']', ')').replace('{', '(').replace('}', ')')
print(int(eval(str_in)))




# 方法二：迭代输出解法
st = input().replace('[', '(').replace(']', ')').replace('{', '(').replace('}', ')')


def func(i):
    nums = []
    flag = None
    while i < len(st):
        num = 0
        if st[i] == '(':
            i, num = func(i + 1)
        if flag == ')':
            return i, sum(nums)

        while i < len(st) and st[i].isdigit():  #第一个st[0] = 3是数字
            num = num * 10 + int(st[i])
            i += 1  # 只要i为数字就直接计算出数字的值。然后将num加入数组
        if not nums:  # 如果nums为空，将当前num加入nums
            nums.append(num)
        if flag == '+':
            nums.append(num)
        elif flag == '-':
            nums.append(-num)
        elif flag == '*':
            nums.append(nums.pop() * num)  #如果是乘法和除法优先进行计算，将最后输入（需要先乘除计算的值）的值先pop出来计算，然后将计算结果append
        elif flag == '/':
            nums.append(nums.pop() // num)
        if i < len(st):
            flag = st[i]  # flag表示当前的非数字字符,第一个是st[1]是+号
        i += 1  #继续增加进行计算
    return i, sum(nums)



print(func(0)[1]) #输出sums