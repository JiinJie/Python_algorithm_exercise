# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 10:02
# @Author  : jinjie
# @File    : 005_数组合并_200.py

"""
题目
现在有多组整数数组，需要将他们合并成一个新的数组。
合并规贝刂：
·从每个数纟且里按顺序取出固定长度的内容合并到新的数组中，取完的内容会删除掉，
·如果该行不足固定长度或者已经为空，则直接取出剩余部分的内容放到新的数组中，继续下一行
如样例1，获得长度3，先遍历第一行，获得 2，5，6；
再遍历第二行，得1，7，4；
再循环回到第一行，获得7，9，5；
再遍历第二行，狄得3，4；
再回到第一行，狄得7，
按顺序拼接成最终结果。
"""

get_len = int(input())
get_nums = int(input())

all_list = []
res = []
for k in range(get_nums):
    get_list = list(map(int,input().split(",")))
    all_list.append(get_list)


# #print(all_list)
# # 方法一：使用索引操作
# index = 0
# while len(all_list)>0:
#     link_list = all_list[index]  #使用索引加减，避免for循环，降低复杂度
#     for _ in range(get_len):
#         if len(link_list) == 0:
#             all_list.pop(index)
#             index -= 1
#             break
#         res.append(link_list.pop(0))
#     index += 1
#     if index >= len(all_list):
#         index = 0
#
# print(res)


# 方法二：直接使用嵌套for循环
list_len = len(all_list)
while list_len>0:
    for i in range(list_len):
        if i >= list_len:  #判断是否超出数组长度
            i -= 1          #如果超出，-1,计算上一个需要的值(循环内已经将空数组pop)
        for _ in range(get_len):
            if len(all_list[i]) == 0:
                all_list.pop(i)
                list_len -= 1
                break
            #else: #如果不满足直接跳出内层循环
            res.append(all_list[i].pop(0))



print(res)
