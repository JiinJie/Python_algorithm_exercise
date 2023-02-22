# -*- coding: utf-8 -*-
# @Time    : 2023/2/22 14:44
# @Author  : jinjie
# @File    : 023_第K个排列_100.py

"""
题目描述
给定参数n，从1到n会有n个整数：1，2，3，一，n，这n个数字共有n！种排列。
按大小顺序升序列出所有排列的情况，并一一标记，
当n=3时，所有排列如下：
“123” “132” “213” “231” “312” “321”
给定n和k，返回第k个排列。
参考三种解法：
https://leetcode.cn/problems/permutation-sequence/solution/python3-chao-xiang-xi-duo-jie-fa-by-ting-ting-28-3/
"""

# # 方法一:使用permutations
# import itertools
#
# n = int(input())
# k = int(input())
# res = ""
#
# a = range(1, n + 1)
# res_list = list(itertools.permutations(a))  # 使用内置函数permutations进行全排列
# # print(res_list)
#
#
# for i in res_list[k - 1]:
#     res += str(i)
# print(res)



# 方法二：迭代输出
def getPermutation(n, k):
    def get_n(n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res  #获取第一个值

    ret, nums = '', list(map(str, list(range(1, n + 1))))
    for i in range(n, 0, -1):
        res = get_n(i - 1)
        index = (k - 1) // res
        ret += nums.pop(index)  #获取结果相应索引的值，重新组合
        k -= res * index
    return ret


n = input()
k = input()
print(getPermutation(int(n), int(k)))



# 解法三；暴力解法

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n + 1)]
        for i in range(k - 1):
            self.permute(nums)
        return "".join([str(i) for i in nums])

    def permute(self, nums: list) -> None:
        run = False
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                for k in range(len(nums) - 1, 0, -1):
                    if nums[k] > nums[i - 1]:
                        nums[k], nums[i - 1] = nums[i - 1], nums[k]
                        nums[i:] = nums[i:][::-1]
                        return



"""
举例来说明。

n = 4， 参与排列的数字「1， 2， 3， 4」

列出所有的排列

1 + (permutations of 2, 3, 4)
2 + (permutations of 1, 3, 4)
3 + (permutations of 1, 2, 4)
4 + (permutations of 1, 2, 3)

n个数字的排列数为n!,那么3个数的排列数为6。假如k=14，那么第14个排列落在

3 + (permutations of 1, 2, 4)

令k=14-1(减去1是因为程序中索引从0开始), k/(n-1)!= 13/(4-1)! = 2, 在数列「1， 2， 3， 4」中索引为2的数字为3，所以第一个数字为3。
那么问题进一步缩小为「1， 2， 4」数字的排列，求第 k= k%(n-1)!=13%(4-1)=1 个排列：

1 + (permutations of 2, 4)
2 + (permutations of 1, 4)
4 + (permutations of 1, 2)

在这一步中，2个数字排列有2!， 总共有3*2!=6个，我们寻找第一个排列，那么落在

1 + (permutations of 2, 4)

此时 k/(n-2)! = 1/(4-2)! = 0, 即「1， 2， 4」中索引0的数字1。目前我们知道前面两个数字3，1。剩下的数字依次类推。

剩余：「2, 4」

k = k % (n-2)! = 1%(4-2)! = 1，第三个数字在「2， 4」中的索引为 k/(n-3)!= 1/(4-3)! = 1，所以第三个数字为4

剩余：「2」

k = k % (n-3)! = 1%(4-3)! = 0，第四个数字在「2」中的索引为 k/(n-4)!= 0/(4-4)! = 0，所以第四个数字为2

"""