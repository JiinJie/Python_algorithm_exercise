# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 12:56
# @Author  : jinjie
# @File    : 017_整数分解_base.py

num = int(input())

res = []
for i in range(1,num):
    sum = 0
    temp = []
    for j in range(i,num):
        sum += j
        if sum == num:
            temp.append(j)
            res.append(f"{num}={'+'.join(map(str,temp))}")
            break  #如果存在直接加入res,同时跳出循环
        temp.append(j)

print(f"{num}={num}")
res.sort(key=len)
for r in res:
    print(r)
print(f"Result:{len(res)+1}")