# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 14:07
# @Author  : jinjie
# @File    : 021_众数和中位数_100.py

"""
机试题目
1．众数是指一组数据中出现次数多的数
众数可以是多个
2，中位数是指扌巴一组数据从小到大排列，最中间的那个数，
如果这组数据的个数是奇数，那最中间那个就是中位数
如果这组数据的个数为偶数，那就吧中间的两个数之和除以2就是中位数
3，查找整型数组中元素的众数并纟且成一个新的数组
求新数组的中位数
"""

list_in = list(input().split())
temp_dict = {}
new_list = []

for i in list_in:
    if temp_dict.get(i):
        if i not in new_list:
            new_list.append(i)
    else:
        temp_dict[i] = 1

new_list.sort()
len_list = len(new_list)


ii = int(len_list/2)
if len_list%2 == 0:
    res = int((int(new_list[ii]) + int(new_list[ii+1]))/2)
else:
    res = int(new_list[ii])

print(res)