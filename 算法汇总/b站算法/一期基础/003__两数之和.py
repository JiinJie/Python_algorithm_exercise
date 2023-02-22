# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 11:46
# @Author  : jinjie
# @File    : 003__两数之和.py
"""
给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
"""
from typing import List

# 用一个dict储存每一个数对应的下标，时间复杂度为O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}
        result = []
        for i,num in enumerate(nums):
            if target - num in temp_dict:
                """
                如果当前循环的target - num 的值已经在字典中则直接返回，
                否则将该值写入字典缓存,供下一个num进行比对
                """
                result = temp_dict[target-num],i  # 返回结果
            temp_dict[nums[i]] = i  #值作为key,索引写入字典，作为value
        return result


a = Solution().twoSum(nums=[2,7,11,15],target=9)
print(a)



# 暴力循环求解【时间复杂度高，不推荐】
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # enumerate内置函数 用于获取index和value
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums[i+1:]):
                if num1 + num2 ==target:
                    return i,j+i+1 #切片后的j索引变为0,需要加上i+1


# a = Solution2().twoSum(nums=[2,7,11,15],target=9)
# a = Solution2().twoSum(nums = [3,3], target = 6)
# print(a)