# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 16:57
# @Author  : jinjie
# @File    : HJ48_从单向链表中删除指定值的节点.py

"""
输入一个单向链表和一个节点的值，从单向链表中删除等于该值的节点，删除后如果链表中无节点则返回空指针。

链表的值不能重复。

构造过程，例如输入一行数据为:
6 2 1 2 3 2 5 1 4 5 7 2 2
则第一个参数6表示输入总共6个节点，第二个参数2表示头节点值为2，剩下的2个一组表示第2个节点值后面插入第1个节点值，为以下表示:

"""

str_in = list(input().split(' '))
#print(str_in)

link_len = int(str_in[0])
link_head = str_in[1]
link = str_in[2:-1]
link_delete = str_in[-1]
#print(link)
temp_list = [link_head]

# def get_index(list,value):
#     for index, value in enumerate(list):
#         if value == 0:
#             return index



for i in range(0,len(link),2):
    #index = get_index(temp_list,link[i+1])
    #print(link[i+1])
    index = temp_list.index(link[i+1])
    #print(index)
    temp_list.insert(index+1,link[i])

temp_list.remove(link_delete)
for i in temp_list:
    print(i,end=' ')

