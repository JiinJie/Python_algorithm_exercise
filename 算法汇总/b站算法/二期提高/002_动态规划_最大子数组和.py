# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 22:26
# @Author  : jinjie
# @File    : 002_动态规划_最大子数组和.py

"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。
"""
from typing import List

"""
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
"""

from copy import copy
# 自己写的版本
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        temp_list = copy(nums)
        res = temp_list[0]
        for i in range(len(nums)):
            if i == 0:
                pass
            else:
                temp_list[i] = temp_list[i-1]+nums[i]
                if temp_list[i] < nums[i]:
                    temp_list[i] = nums[i]
                else:
                    pass
            if res < temp_list[i]:
                res = temp_list[i]
        return(res)

# 标准版【代码优化】
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)  #开辟空间，复制列表元素
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            res = max(res, dp[i])
        return res


if __name__ == '__main__':
    list_in = [-2,1,-3,4,-1,2,1,-5,4]
    Solution().maxSubArray(list_in)
