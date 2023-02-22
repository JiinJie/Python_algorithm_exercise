# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 19:38
# @Author  : jinjie
# @File    : HJ67_24点游戏算法.py

"""
给出4个1-10的数字，通过加减乘除运算，得到数字为24就算胜利,除法指实数除法运算,
运算符仅允许出现在两个数字之间,本题对数字选取顺序无要求，但每个数字仅允许使用一次，且需考虑括号运算
此题允许数字重复，如3 3 4 4为合法输入，此输入一共有两个3，但是每个数字只允许使用一次，则运算过程中两个3都被选取并进行对应的计算操作。
"""

import copy


def dps(num):
    if len(num) == 1:
        return abs(abs(num[0]) - 24) < 0.00001
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            n1, n2 = num[i], num[j]
            rst = num[:i] + num[i + 1:j] + num[j + 1:]
            #如果对前两个进行计算后的值，再对后两个进行迭代计算，当满足条件时直接返回True
            if dps([n1 + n2] + rst): return True
            if dps([n1 - n2] + rst): return True
            if dps([n1 * n2] + rst): return True
            if n1 != 0:
                if dps([n2 / n1] + rst):
                    return True
            if n2 != 0:
                if dps([n1 / n2] + rst):
                    return True
    return False


while True:
    try:
        #x = list(map(int, input().split()))
        x = [7,2,1,10]
        print("true" if dps(x) else "false")
    except:
        break