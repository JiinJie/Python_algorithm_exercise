# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 22:05
# @Author  : jinjie
# @File    : 001_动态规划_斐波那契数列.py

import numpy as np

# 动态规划实现--[由于python数组定义问题，无法使用该代码实现]
# class Solution:
#     def fib(self, n: int) -> int:
#         if n <= 1:
#             return n
#
#         dp = []  #注：python中的空列表不可以直接赋值
#         dp = [0,1]
#         for i in range(n):
#
#             #dp[i] = dp[i - 1] + dp[i - 2]
#             dp.append(dp[i - 1] + dp[i - 2])
#         return dp[n]

# 动态规划实现
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p, q = q, r
            r = p + q

        return r


a = Solution().fib(5)
print(a)
