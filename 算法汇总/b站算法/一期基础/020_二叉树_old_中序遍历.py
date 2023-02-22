# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 16:58
# @Author  : jinjie
# @File    : 020_二叉树_old_中序遍历.py

"""
二叉树_中序遍历
"""

from typing import Optional,List,Union
from collections import deque



# 方法一：递归
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def gen_tree(values: list) -> Union[TreeNode, None]:
    if not values:
        return None
    iter_value = iter(values)
    root = TreeNode(next(iter_value))
    d = deque()
    d.append(root)
    while 1:
        head = d.popleft()
        try:
            head.l_node = TreeNode(next(iter_value))
            d.append(head.l_node)
            head.r_node = TreeNode(next(iter_value))
            d.append(head.r_node)
        except StopIteration:
            break
    return root


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,rst = [root],[]
        while stack:
            i = stack.pop()
            if isinstance(i,TreeNode):
                stack.extend([i.right,i.val,i.left])
            elif isinstance(i,int): #如果i是int则
                rst.append(i)
        return rst





# 方法二：循环遍历



if __name__ == '__main__':
    root_list = [1,None,2,3]
    root = gen_tree(root_list)
    a = Solution().inorderTraversal(root)
    print(a)
