# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 10:57
# @Author  : jinjie
# @File    : 003_动态规划_买卖股票最佳时机.py

"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
"""
"""
创建一个二维数组 dp[i][j] 。 i表示第几天，j表示是否持股，0为不持股，1为持股。dp[i][j]则为第i天是否持股而获得的利润，
j =0，即不持股有两种情况，一是没买入，二是已经卖出
dp[i] = max(dp[i-1][0],dp[i-1][1]+prices[i])

j = 1，即持股有两种情况，一是昨天到今天一直持股，二是昨天买入，今天持股
dp[i] = max(dp[i-1][1],prices[i])
"""

from typing import  List
# 解法一：动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        list_len = len(prices)
        dp_0 = [0] * list_len  # 为了不创建二维数组，直接使用两个数组存放两种状态的值
        dp_1 = [0] * list_len
        dp_1[0] = -prices[0]

        if list_len < 2:
            return 0

        for i in range(1, list_len):
            dp_0[i] = max(dp_0[i - 1], dp_1[i - 1] + prices[i])
            dp_1[i] = max(dp_1[i - 1], -prices[i])
        return dp_0[list_len - 1]  # 只返回dp_0 的最大值，因为只有j=0时股票才会卖出，才能获利
        # print(dp_0)
        # print(dp_1)

# 解法二：不使用数组存值的动态规划
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)#表示正无穷大
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit