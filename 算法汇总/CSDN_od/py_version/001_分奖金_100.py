# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 11:50
# @Author  : jinjie
# @File    : 001_分奖金_100.py

"""
题目
公司老板做了一笔大生意，想要给每位员工分配一些奖金，想通过游戏的方式来决定每个人分多少钱。
按照员工的工号顺序，每个人随机抽取一个数字。按照工号的顺序往后排列，遇到第一个数字比自己数字大的，那么，前面的员工就可以
获得距离米数字差值的奖金。
如果遇不到比自己数字大的，就给自己分配随机数数量的奖金。
例如：
按照工号顺序的随机数字是：2，10，3。那么第2个员工的数字10比第1个员工的数字2大，
所以，第1个员工可以获得1*（10-2）=8
第2个员工后面没有比他数字更大的员工，所以，他获得他分配的随机数数量的奖金，就是10。
第3个员工是最后一个员工，后面也没有比他更大数字的员工，所以他得到的奖金是3。
请帮老板计算一下每位员工最终分到的奖金都是多少钱。
"""


# 方法一：嵌套for循环 复杂度 o(n)^2
import copy

n = int(input())
str_in = list(map(int,input().split()))
bons = []

for i in range(len(str_in)):
    for j in range(i+1,len(str_in)):
        if str_in[j] > str_in[i]:
            bons.append((j-i)*(str_in[j]-str_in[i]))
            break  #js中 continue outter;
    else:  #在for循环中使用else，当条件不满足时可以跳出当前循环
        bons.append(str_in[i])


print(bons)


# 方法二：单调栈 复杂度 o(n)
import copy

n = int(input())
str_in = list(map(int,input().split()))
stack = []
bons = copy.deepcopy(str_in)

for i in range(len(str_in)):
    while stack and str_in[i]>str_in[stack[-1]]:  #str_in[stack[-1]]记录的是上一个i对应的值
        _index = stack.pop()
        bons[_index] = (i-_index)*(str_in[i]-str_in[_index])  #i是当前索引 _index是前个值（比当前小的）的索引
    stack.append(i)  #stack存放的是索引


print(bons)

