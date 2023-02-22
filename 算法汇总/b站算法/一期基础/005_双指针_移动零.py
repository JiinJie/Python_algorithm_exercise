# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 15:08
# @Author  : jinjie
# @File    : 005_双指针_移动零.py


"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""
from typing import List

# 只遍历一次 快速排序【标准答案】
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        if nums == [0]:
            print("数组为0")
            return nums
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1


# # 方法二 有bug，必须要循环两次，不能直接赋0
# class Solution2:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if nums == None:
#             return
#         if len(nums) == 1:
#             return nums
#         j = 0
#         for i in range(len(nums)): #默认从1开始
#             print(j)
#             if nums[i]:
#                 nums[j] = nums[i]
#                 nums[i] = 0
#                 j += 1  # 不管是不是零都需要继续+1
#         return nums



# 方法三 遍历两次
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums ==  None:
            return

        j = 0
        for i in range(len(nums)):
            print(j)
            if nums[i]:
                nums[j] = nums[i]
                j += 1  # 不管是不是零都需要继续+1

        for i in range(j, len(nums)):
            nums[i] = 0
        return nums

a = Solution().moveZeroes([0])
print(a)
