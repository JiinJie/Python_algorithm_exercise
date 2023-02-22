# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 13:24
# @Author  : jinjie
# @File    : 004_双指针_合并两个有序数组.py

"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

"""
from typing import List

"""通过倒序排列将最大值追加在nums1中末尾"""

# 该方法只要遍历一次数组即可，时间复杂度较低
# 同时该方法不需要创建临时数组，空间复杂度比 m+n 小。直接是nums1 的m即可


# 优化版
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m+n
        for i in range(k,1):
            if nums1[n-1] < 0:
                nums1[k-1] = nums2




# 原版
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:  # 若nums1中最后一个元素大于nums2[]中最后一个元素
                nums1[m + n - 1] = nums1[m - 1]  # 则扩展后的列表最后一个元素是俩元素中最大的
                m -= 1  # nums1中元素-1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:  # 若nums1完了，nums2还没完
            nums1[:n] = nums2[:n]


# 直接合并然后排序【会报错】，因为nums1可能比nums2小

# class Solution3:
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         for num in nums2:
#             nums1[m] = num
#             m += 1
#         nums1.sort()

