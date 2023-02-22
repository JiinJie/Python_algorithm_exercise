# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 14:26
# @Author  : jinjie
# @File    : 022_人数最多的站点_100.py

nums = int(input())
temp_dict = {}

while nums:
    start_, end_ = input().split()
    #print(start_,end_)
    for i in range(int(start_),int(end_)+1):
        if temp_dict.get(i):
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1


    nums -= 1
print(temp_dict)
print(min(temp_dict.values()))