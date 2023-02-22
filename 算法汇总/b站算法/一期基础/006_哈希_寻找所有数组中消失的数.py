# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 16:01
# @Author  : jinjie
# @File    : 006_哈希_寻找所有数组中消失的数.py

"""
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。
"""
"""示例 1：
输入：nums = [4,3,2,7,8,2,3,1] # 此时区间为 [1~8] 则没有出现的数字为5，6
输出：[5,6]
"""

"""示例 2：
输入：nums = [1,1]  # 此时区间为 [1~2] 则没有出现的数字为2
输出：[2]
"""
from typing import List

# 方法一 在不适用额外空间且时间复杂度为O（n）的情况下解决这个问题
"""让nums本身充当哈希表，对数组所有值+n"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result_list = []

        for num in nums:
            x = (num-1)%n  # 对该num取余，防止该值已经被+n。作为索引
            nums[x] += n  # 获取nums中该x索引的值进行+n操作
        for i in range(n):  # 再次循环数组查找没有被+n的索引
            if nums[i] <= n:
                result_list.append(i+1)  # 该索引值+1 即为该数组中未出现的值

        return result_list


# 方法二 使用hashmap暂存
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp_dict = {}
        temp_list = []
        for i,num in enumerate(nums):
            if i in num:
                temp_dict[nums]=i
                print(num)
            else:
                temp_dict[nums[i]]=i  # 将list的value值作为dict的key
        return temp_list


a = Solution().findDisappearedNumbers(nums=[1,1])
print(a)

