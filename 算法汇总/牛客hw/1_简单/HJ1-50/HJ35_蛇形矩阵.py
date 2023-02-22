# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 21:05
# @Author  : jinjie
# @File    : HJ35_蛇形矩阵.py

"""
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
"""

# 方法一：公式法
n = int(input())
for i in range(1,n+1) :
    for j in range(i,n+1) :
        print(int(((j+j**2)/2)-i+1),end = ' ')
    print()
"""
观察第一行的规律符合累加求和公式；(n+1)n/2
第二行的规律则是第一行的 ((n+1)n/2) - 1
第三行的规律则是第一行的 ((n+1)n/2) - 2
第四行的规律则是第一行的 ((n+1)n/2) - 3
当i = 1 时，j = 1,2,3,4 进入循环；
当i = 2 时，j = 2,3,4
当i = 3 时，j = 3,4
当i = 4 时，j = 4
"""

# 方法二:二维数组法
while True:
    try:
        num = int(input()) #输入num
        a = []
        for i in range(num):
            a.append([0]*num) #先创建一个num*num的二维列表
        for i in range(num):
            for j in range(num - i): #遍历整个上三角矩阵
                if(j == 0):
                    if(i == 0):
                        a[i][j] = 1 #a[0][0] = 1
                    else:
                        a[i][j] = a[i-1][j] + i #第一列的值为上一行的值加上行数
                else:
                    a[i][j] = a[i][j - 1] + i + j + 1 #不是第一列的值为本行的上一列加上本行数（指的是在矩阵中存储的行数（i））加本列数(j) + 1
        for i in range(num):
            for j in range(num - i):
                print(a[i][j],end = ' ') #输出上三角矩阵
            print('\r') #每输出一行回车
    except:
        break


