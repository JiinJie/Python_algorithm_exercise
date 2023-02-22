# -*- coding: utf-8 -*-
# @Time    : 2023/2/16 10:23
# @Author  : jinjie
# @File    : HJ69_矩阵乘法.py

"""
如果A是个x行y列的矩阵，B是个y行z列的矩阵，把A和B相乘，其结果将是另一个x行z列的矩阵C。这个矩阵的每个元素是由下面的公式决定的
"""
"""
矩阵算法： 矩阵A的横向*矩阵B的竖向，然后相加，作为乘积矩阵的结果
"""
while True:
    try:

        x = int(input())
        y = int(input())
        z = int(input())

        list1 = []
        list2 = []
        list3 = [[0]*z for _ in range(x)]

        for _ in range(x):
            list1.append(list(map(int,input().split())))

        for _ in range(y):
            list2.append(list(map(int,input().split())))
        # print(list1)
        # print(list2)
        #print(list3)

        for i in range(x):
            for k in range(z):
                for j in range(y):
                    list3[i][k] += list1[i][j] * list2[j][k]
                    #print(f"{list1[i][j]}*{list2[j][k]}")

        for i in range(x):
            for k in range(z):
                print(list3[i][k],end=' ')
            print('')
    except:
        break
#print(list3)