# -*- coding: utf-8 -*-
# @Time    : 2022/8/30 16:49
# @Author  : jinjie
from bisect import bisect_left

"""
二分查找某个列表中的值
使用了python自带的库 bisect
"""

nums = [5,7,7,8,8,10]
target = 7

def searchRange(nums,target):
    l = bisect_left(nums, target)
    r = bisect_left(nums, target + 1)
    return [-1, -1] if l == len(nums) or l >= r else [l, r - 1]

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 7
    searchRange(nums,target)
