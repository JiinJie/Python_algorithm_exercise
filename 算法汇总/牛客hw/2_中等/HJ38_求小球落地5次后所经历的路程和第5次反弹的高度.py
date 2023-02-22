# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 12:10
# @Author  : jinjie
# @File    : HJ38_求小球落地5次后所经历的路程和第5次反弹的高度.py

"""
假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下,
求它在第5次落地时，共经历多少米?第5次反弹多高？
"""
init_height = int(input())

current_height = init_height
res = 0
for i in range(5):
    #res += current_height+current_height/2
    current_height = current_height/2
    #print(current_height)
    res += current_height*3

print(res-current_height)
print(current_height)