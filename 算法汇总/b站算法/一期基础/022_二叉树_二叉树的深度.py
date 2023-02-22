# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 15:21
# @Author  : jinjie
# @File    : 022_二叉树_二叉树的深度.py


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


#迭代获取二叉树的深度
def get_depth(node):
    if node is None:
        return 0
    dl = get_depth(node.left)
    dr = get_depth(node.right)

    return max(dl,dr)+1

from collections import deque # python中自带的双端队列
#使用层序遍历获取二叉树深度
def get_depth2(root):
    q = deque([(root,1)]) #设置根节点的深度为1
    while q:
        node,d = q.popleft()
        if node.left:
            q.append((node.left,d+1))  #存在任意子树则深度+1
        if node.right:
            q.append((node.right,d+1)) #存在任意子树则深度+1

    return d


if __name__ == '__main__':
    root =list_to_binarytree(list_tree)
    print(get_depth(root))
    print(get_depth2(root))

