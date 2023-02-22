# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 18:25
# @Author  : jinjie
# @File    : 032_贪心算法_三角形的最大周长.py

"""
给定由一些正数（代表长度）组成的数组arr，返回由其中三个长度组成的、面积不为零的三角形的最大周长
如果不能形成任何面积不为零的三角形，返回 `0`
"""
"""
三角形两边之和大于第三边  a+b >c，c>a，c>b
将数组升序排序，倒序寻找最大的三个数，查看是否满足上述条件。
如果最大的三个数，即a+b <=c 那么在数组中无法构成以c为边的三角形【a,b之和已经是最大的了】
"""

from  typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums)< 3:
            return 0
        else:
            nums.sort()
            for i in range(len(nums)-1,1,-1):
                print(nums[i],nums[i-1],nums[i-2])
                if nums[i] < nums[i-1] +nums[i-2]:
                    print(nums[i])
                    zhouchang = nums[i]+nums[i-1]+nums[i-2]
                    return zhouchang
            return 0

a = Solution().largestPerimeter([3,6,2,3])
print(a)