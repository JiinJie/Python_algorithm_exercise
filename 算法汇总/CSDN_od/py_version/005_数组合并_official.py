# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 11:15
# @Author  : jinjie
# @File    : 005_数组合并_official.py
import re

def solve_method(k, n, strings):
    builder = ""
    lists = [list(map(int, string.split(","))) for string in strings]
    index = 0
    while len(lists) > 0:
        linked_list = lists[index]
        for i in range(k):
            if len(linked_list) == 0:
                lists.pop(index)
                index -= 1
                break
            builder += str(linked_list.pop(0)) + ","
        index += 1
        if index >= len(lists):
            index = 0
    return builder[:-1]

k = int(input().strip())
n = int(input().strip())
strings = [input().strip() for i in range(n)]
res = solve_method(k, n, strings)
print(res)
