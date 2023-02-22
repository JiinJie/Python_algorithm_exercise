# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 11:47
# @Author  : jinjie
# @File    : HJ53_杨辉三角形的变形.py

"""
以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数、左上角数和右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。
求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。例如输入3,则输出2，输入4则输出3，输入2则输出-1。
如图：
https://uploadfiles.nowcoder.com/images/20210617/557336_1623898240633/9AC4B89B5E22854D71DEA4CA6EBD6F9F
"""

alt = [2,3,2,4]  #表示出现的位置，2表示第二个

while True:
    try:
        n = int(input())
        if n<3:
            print(-1)
        if n>=3:
            print(alt[(n-3)%4])
    except:
        break