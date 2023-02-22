# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 15:49
# @Author  : jinjie
# @File    : 011_深度-二叉树最小深度.py



from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 深度算法-基础版【待优化】
class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left is None and root.right is None:
            return 1
        min_num = int(1e9) #初始化为最大值
        if root.left != None:
            min_num = min(self.minDepth(root.left),min_num)
        if root.right != None:
            min_num = min(self.minDepth(root.right),min_num)
        return min_num + 1

# 深度算法-优化版【推荐】
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left:
            return 1+self.minDepth(root.right)
        if not root.right:
            return 1+self.minDepth(root.left)
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        res = 1+min(left,right)
        return res