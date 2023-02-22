# -*- coding: utf-8 -*-
# @Time    : 2023/2/16 11:31
# @Author  : jinjie
# @File    : H70_矩阵乘法计算量估算.py

"""
矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：
A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵
计算A*B*C有两种顺序：((AB)C)或者(A(BC))，前者需要计算15000次乘法，后者只需要3500次。
编写程序计算不同的计算顺序需要进行的乘法次数。
"""

while True:
    try:
        n = int(input())
        arr = []
        order = []
        res = 0
        for i in range(n):
            arr.append(list(map(int,input().split())))
        #print(arr)

        f = input()
        for i in f:
            if i.isalpha():
                order.append(arr[ord(i)-65]) #将字母按照ascii进行排序区分
            elif i == ')' and len(order) >= 2:  # 栈，先读取到右括号，先出栈。直至读完所有的右括号
                b = order.pop()   #用b和a分别代表最后的两个值，然后进行四则运算
                a = order.pop()
                res += a[1]*b[1]*a[0]
                order.append([a[0],b[1]])

        print(res)
    except:
        break