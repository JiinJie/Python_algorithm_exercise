# -*- coding: utf-8 -*-
# @Time    : 2022/8/18 15:18
# @Author  : jinjie

# 输出9*9乘法口诀表
def chengfa():
    for x in range(1,10):
        for j in range(1,x+1):
            print(f"{x}*{j}={x*j}",end=' ')
            if x == j:
                print('\n')


def diedai():
    a = [x for x in range(1, 11) if x % 2 == 0]
    print(a)

if __name__ == '__main__':
    diedai()