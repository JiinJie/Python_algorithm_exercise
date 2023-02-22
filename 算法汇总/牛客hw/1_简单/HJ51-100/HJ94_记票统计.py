# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 11:01
# @Author  : jinjie
# @File    : HJ94_记票统计.py

"""
请实现一个计票统计系统。你会收到很多投票，其中有合法的也有不合法的，请统计每个候选人得票的数量以及不合法的票数。
（注：不合法的投票指的是投票的名字不存在n个候选人的名字中！！）
数据范围：每组输入中候选人数量满足 1≤n≤100  ，总票数量满足 1≤n≤100
"""

# 接收参数
vote_num = int(input())
vote_name = list(input().split())
people_num = int(input())
people_name = list(input().split())

# 初始化字典
temp_dict = {}
for i in vote_name:
    temp_dict[i] = 0
temp_dict['Invalid'] = 0

#数据写入字典
for i in people_name:
    #print(i)
    if temp_dict.get(i) !=None:
        temp_dict[i] += 1
    else:
        temp_dict['Invalid'] +=1
# 输出结果
for key,value in temp_dict.items():
    print(f"{key} : {value}")