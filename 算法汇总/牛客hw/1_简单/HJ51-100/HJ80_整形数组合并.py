# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 17:50
# @Author  : jinjie
# @File    : HJ80_整形数组合并.py



len_list1 = int(input())
list1 = list(input().split())
len_list2 = int(input())
list2 = list(input().split())
#print(list1,list2)

res = ""
list1.extend(list2)
list1.sort()
for i in range(len(list1)):
    if i == 0:
        res += list1[0]
    elif list1[i] == list1[i-1]:
        pass
    else:
        res += list1[i]

print(res)