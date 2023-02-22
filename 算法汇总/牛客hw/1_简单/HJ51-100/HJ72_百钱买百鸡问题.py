# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 16:37
# @Author  : jinjie
# @File    : HJ72_百钱买百鸡问题.py


"""
公元五世纪，我国古代数学家张丘建在《算经》一书中提出了“百鸡问题”：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
现要求你打印出所有花一百元买一百只鸡的方式。
"""
while True:
    try:
        input().isalnum()
        for i in range(21): #i为公鸡
            for j in range(1,50):
                for k in range(1,100):
                    sum = i*5+j*3+k/3
                    if sum == i+k+j and sum ==100:
                        print(i,j,k)

    except:
        break