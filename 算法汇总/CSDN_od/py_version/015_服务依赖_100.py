# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 19:41
# @Author  : jinjie
# @File    : 015_服务依赖_100.py

# class Node:
#     def __init__(self,head=1,value=0,next=None):
#         self.head = head
#         self.value = value
#         self.next = next
#
# # 如果节点故障则将其value置为1






# 使用嵌套列表存储，如果关联则加在关联后的列表内
str_list = list(input().split(","))
bad_list = list(input().split(','))

# print(str_list)
# print(bad_list)
temp_list = []

for i in str_list:
    temp_list.append(list(i.split("-")))

print(temp_list)

relat_list = []
relat_list.append(temp_list[0][0])
relat_list.append(temp_list[0][1])
temp_list.pop(0)

for i in temp_list:
    if relat_list[-1] == i[0]:
        relat_list.append(i[1])
        temp_list.remove(i)

