# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 14:21
# @Author  : jinjie
# @File    : 004_动态规划_使用rand7实现rand10.py
"""
给定方法 rand7 可生成 [1,7] 范围内的均匀随机整数，试写一个方法 rand10 生成 [1,10] 范围内的均匀随机整数。
你只能调用 rand7() 且不能调用其他方法。请不要使用系统的 Math.random() 方法。
每个测试用例将有一个内部参数 n，即你实现的函数 rand10() 在测试时将被调用的次数。请注意，这不是传递给 rand10() 的参数。
"""

"""
先 计算rand7-1 的值 ，范围 0~6 ，
在乘以7 (rand7-1)*7  可以得到 0，7，14，21，28，35，42
再加上 rand7-1 可以得到 0~48 ，一共49个数
然后 通过if判断，如果大于40则重新生成，只保留rand40，
然后 通过%取余 得到 ran10
rand 7 --> rand 49 --> rand 40 --> rand10 
"""

# 方法一：通过rand7乘积和加减变化得到
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        temp = 40
        while(temp >= 40):
            temp = (rand7()-1)*7 + rand7() -1
        return temp%10 +1


# 直接通过rand7进行加减
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        temp = rand7()
        while temp == 7:
            temp = rand7()
        res = rand7()
        while res > 5:
            res = rand7()
        return res if temp > 3 else res + 5