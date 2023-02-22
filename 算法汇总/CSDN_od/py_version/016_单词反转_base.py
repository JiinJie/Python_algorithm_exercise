# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 10:59
# @Author  : jinjie
# @File    : 016_单词反转_base.py

str_in = list(input().split())
start_ = int(input())
end_ = int(input())

stack = []
res = []
for i in range(len(str_in)):
    if start_ <= i <= end_:
        stack.append(str_in[i])
        if i==end_ or i == len(str_in)-1:
            for _ in range(len(stack)):
                res.append(stack.pop())
    else:
        res.append(str_in[i])


for i in res:
    print(i,end=' ')

