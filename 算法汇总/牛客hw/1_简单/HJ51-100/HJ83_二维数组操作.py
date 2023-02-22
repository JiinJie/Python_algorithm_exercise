# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 20:32
# @Author  : jinjie
# @File    : HJ83_二维数组操作.py
"""
有一个m∗n 大小的数据表，你会依次进行以下5种操作：
1.输入m 和n ，初始化m∗n 大小的表格。
2.输入 x1,y1,x2,y2 交换坐标在（x1,y1）(x2,y2)的两个数。
3.输入x ，在第x 行上方添加一行。
4.输入y ，在第y 列左边添加一列。
5.输入x,y ，查找坐标为(x,y) 的单元格的值。
请编写程序，判断对表格的各种操作是否合法。
详细要求:
1.数据表的最大规格为9行*9列，对表格进行操作时遇到超出规格应该返回错误。
2.对于插入操作，如果插入后行数或列数超过9了则应返回错误。如果插入成功了则将数据表恢复至初始化的m∗n 大小，多出的数据则应舍弃。
3.所有输入坐标操作，对m∗n 大小的表格，行号坐标只允许0~m-1，列号坐标只允许0~n-1。超出范围应该返回错误。
本题含有多组样例输入！行列从0开始标号
数据范围：数据组数：1≤t≤5
进阶：时间复杂度： O(1) ，空间复杂度：O(1)
"""

while True:
    try:
        m,n = map(int,input().split())
        x1,y1,x2,y2 = map(int,input().split())
        insert_x = int(input())
        insert_y = int(input())
        x,y = map(int,input().split())

        if(0<=m<= 9) and(0<=n<=9):
            print('0')
        else:
            print('-1')
        if(0<=x1<m) and(0<=y1<n) and(0<=x2<=m) and(0 <=y2<n):
            print('0')
        else:
            print('-1')
        if (0 <= insert_x < m) and (m < 9):
            print('0')
        else:
            print('-1')
        if (0 <= insert_y < n) and (n < 9):
            print('0')
        else:
            print('-1')
        if(0 <= x < m)and (0 <= y < n):
            print('0')
        else:
            print('-1')
    except:
        break