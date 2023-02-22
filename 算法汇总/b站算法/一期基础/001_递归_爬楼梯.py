# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 10:19
# @Author  : jinjie
# @File    : 001_递归_爬楼梯.py
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""





"""
示例 1：
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
"""

"""
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""
# 解法一 自上而下递归
class Solution1:
    dict1 = {}
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        elif n==2:
            return 2
        elif self.dict1.get(n) is not None:
            # 直接获取dict1[n]时若key不存在会报错。使用get判断key是否存在后再执行
            return self.dict1[n]
        else:
            result = self.climbStairs(n-1)+self.climbStairs(n-2)
            self.dict1[n] = result
            return result


# result = Solution1().climbStairs(5)
# print(f"输出结果{result}")

#  解法二 自下而上循环求解
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        last_step = 2
        last_last_step = 1
        result = 0

        for i in range(3,n+1):
            result = last_step + last_last_step
            last_last_step = last_step
            last_step = result
            # 由底向上累加
        return result


result = Solution2().climbStairs(5)
print(f"输出结果{result}")