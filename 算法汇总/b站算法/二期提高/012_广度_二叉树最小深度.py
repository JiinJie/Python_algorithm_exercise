# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 15:54
# @Author  : jinjie
# @File    : 012_广度_二叉树最小深度.py

from typing import Optional
from collections import deque



# Definition for a binary tree node.
list_tree = [3,9,20,'','',15,7]
class TreeNode:
    def __init__(self,val=0,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_binarytree(list_tree):
    def level(index):
        if index >= len(list_tree) or list_tree[index] is None:
            return None

        root = TreeNode(list_tree[index])
        root.left = level(2*index + 1)
        root.right = level(2*index + 2)
        return root

    return level(0)


def min_depth(root):
    q = deque([(root,1)])   # 初始化deep深度d = 1
    while q: # 当队列元素不为空【如果为空则已经遍历完成】
        node,d = q.popleft() #将左端出列并读取
        if(node.left == None and node.right == None):
            return d
        if node.left:
            q.append((node.left,d+1))  #存在任意子树则深度+1
        if node.right:
            q.append((node.right,d+1)) #存在任意子树则深度+1
    return d




if __name__ == '__main__':

    root = list_to_binarytree(list_tree)
    print(min_depth(root))
