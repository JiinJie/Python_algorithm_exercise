# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 20:38
# @Author  : jinjie
# @File    : 002_去除多余空格_200.py


"""
https://fcqian.blog.csdn.net/article/details/128399275
"""
import copy

# 输入获取
s = input()
arr = list(map(lambda x: list(map(int, x.split())), input().split(",")))


# 算法入口
def getResult(arr, s):
    quotaStart = False
    needDel = []

    for i in range(len(s)):
        if s[i] == " " and s[i - 1] == " " and not quotaStart:
            needDel.append(i)

        if s[i] == "\'":
            quotaStart = not quotaStart

    sArr = list(s)
    ans = copy.deepcopy(arr)

    for d in needDel:
        sArr[d] = ""
        for i in range(len(arr)):
            start = arr[i][0]
            if d < start:
                ans[i][0] -= 1
                ans[i][1] -= 1

    print("".join(sArr))
    print("".join(list(map(lambda x: str(x), ans))))


# 算法调用
getResult(arr, s)