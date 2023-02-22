# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 16:50
# @Author  : jinjie
# @File    : 030_贪心算法_最长连续递增序列.py

"""
给定一个未经排序的整数数组，找到最长且连续递增的子序列，并返回该序列的长度
序列的下标是连续的
"""

import sys
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        start = 0
        #max_val = sys.maxsize
        max_len = 1 #最少也是1个


        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]: #如果是0会越界
                start = i
            max_len = max(max_len,i-start + 1)
        return max_len