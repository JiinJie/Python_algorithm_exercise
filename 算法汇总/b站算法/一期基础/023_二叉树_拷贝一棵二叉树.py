# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 15:39
# @Author  : jinjie
# @File    : 023_二叉树_拷贝一棵二叉树.py

"""
思路：【递归】 先拷贝子节点，然后单独将这个根节点复制，将子节点挂载。
重复以上操作，将子节点作为当前操作的根节点。直到所有元素均被复制
"""
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

def copy_tree(node):
    if node is None:
        return None
    lt = copy_tree(node.left)
    rt = copy_tree(node.right)

    return TreeNode(node.val,lt,rt) # 递归直到为空


# 层序遍历
from collections import deque # python中自带的双端队列
def level0_order(root):
    q = deque([root]) # 根节点入队
    while q: # 当队列元素不为空【如果为空则已经遍历完成】
        node = q.popleft() #将左端出列并读取
        print(node.val)
        if node.left: # 如果有左子树则入队
            q.append(node.left)
        if node.right: # 如果有右子树则入队
            q.append(node.right)


if __name__ == '__main__':
    root =list_to_binarytree(list_tree)
    new_tree = copy_tree(root)
    print(root)
    print(new_tree)
    level0_order(new_tree)



