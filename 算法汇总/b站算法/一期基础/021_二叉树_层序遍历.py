# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 15:10
# @Author  : jinjie
# @File    : 021_二叉树_层序遍历.py

# 按照每一层，从左到右进行遍历

# 通过队列进行实现。【出队当前元素，将他的两个子元素入队】

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
    # 创建二叉树 root
    root = list_to_binarytree(list_tree)

    level0_order(root)