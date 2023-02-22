# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 11:25
# @Author  : jinjie
# @File    : 002_递归_斐波那契数列.py

""" 京东面试
数列满足规律：后一项等于前两项之和。如 1、1、2、3、5、8、13...

"""

"""本题由复杂度要求  O(1)  O(n) O(logn)"""

#修改符合条件版
"""使用迭代循环即可"""
class Solution:
    def Fibonacci(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 1

        last_step = 1
        last_last_step = 1
        result = 0

        for i in range(3,n+1):
            result = last_step + last_last_step
            last_last_step = last_step
            last_step = result

        return result



# 原版
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        dict1 = {}
        if n == 1:
            return 1
        if n == 2:
            return 1
        elif dict1.get(n) is not None:
            return dict1[n]
        else:
            result = self.Fibonacci(n-1)+self.Fibonacci(n-2)
            dict1[n] = result
            return result

