# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 13:16
# @Author  : jinjie
# @File    : 018_字母消消乐_100.py

"""
题目
游戏规则：
输入一个只包含英文字母的字符串，
字符串中的两个字母如果相邻且相同，就可以消除。
在字符串上反复执行消除的动作，
直到无法继续消除为止，此时游戏结束。
输出最终得到的字符串长度。
"""

str_in = input()

stack = []

for i in str_in:
    if len(stack) != 0:
        if i == stack[-1]:
            stack.pop()
            break
    stack.append(i)

print(len(stack))
