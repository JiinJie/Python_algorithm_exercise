# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 11:39
# @Author  : jinjie
# @File    : 006_事件推送.py
"""
题目
同一个数轴x上有两个点的集合A={AI,A2,...,Am}和B={BI,B2,..,Bm}
Ai和Bj均为正整数，A、B已经按照从小到大排好序，A、B均不为空
给定一个距离R（正整数），
列出同时满足如下条件的所有(Ai,Bj）数对：
1，Ai<=Bj
2，Ai，Bj之间的距离小于等于R
3，在满足1，2的情况下，每个Ai只需输出距离最近的Bj
4，输出结果按Ai从小到大的顺序排序
输入
第一行三个正整数m，
第二行m个正整数，
第三行n个正整数，
"""

str_in = input().split()
list_a = list(map(int,input().split()))
list_b = list(map(int,input().split()))

# print(str_in)
# print(list_a)
# print(list_b)
r = int(str_in[-1])


for i in list_a:
    for j in list_b:
        if i <= j and (j-i)<r:
            print(i,j)
            break


