# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 16:28
# @Author  : jinjie
# @File    : 011_静态扫描最优成本_100.py

"""
题目
静态扫描快速识别源代码的缺陷，静态扫描的结果以扫描报告作为输出：
1，文件扫描的成本和文件大小相关，如果文件大小为N，则扫描成本为N个金币
2，扫描报告的缓存成本和文件大小无关，每缓存一个报告需要M个金币
3，扫描报告缓存后，后继再碰到该文件则不需要扫描成本，直接获取缓存结果
给出源代码文件标识序列和文件大小序列，求解采用合理的缓存策略，最少需要的金币数。
输入
第一行为缓存一个报告金币数M，1M00
第二行为文件标识序列：F1,F2,F3...Fn，其中1<=N<=10000，1<=Fi<=1000
第二行为文件大小序列：S1,S2,S3...Sn,其中1<=N<=10000，1<=Si<=10
输出
采用合理的缓存策略，需要的最少金币数
"""
cost = int(input())
list_a = list(map(int,input().split()))
list_b = list(map(int,input().split()))

temp_dict = {}  # 存放次数
temp_cost = {}  # 存放每个文件大小
res = 0

for i in list_a:
    if temp_dict.get(i):
        temp_dict[i] += 1
    else:
        temp_dict[i] = 1
#print(temp_dict)

for j in list_a:
    if temp_cost.get(j):
        pass
    else:
        temp_cost[j] = list_b[j]
#print(temp_cost)

for key,value in temp_dict.items():
    cost_file = int(temp_cost[key])*int(value)
    cost_cache = cost+int(temp_cost[key])
    if cost_file > cost_cache:
        res += cost_cache
    else:
        res += cost_file


print(res)