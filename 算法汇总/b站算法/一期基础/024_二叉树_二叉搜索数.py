# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 16:04
# @Author  : jinjie
# @File    : 024_二叉树_二叉搜索数.py

# 二叉搜索树/二叉排序树 【左子树小于根节点，右子树大于根节点】
# 可以支持快速的查找、插入和删除


class BinsarySearchTree:
    def __init__(self):
        self.root = None

    def search(self,k):
        node,_ = self.search_father(k)
        return node
        # 避免冗余直接使用search_father
        # node = self.root
        # while node and node.val != k: #判断是否存在当前值
        #     if k < node.val:   #如果比当前节点值小，则继续找他的左子树
        #         node = node.left
        #     else:               #如果比当前节点值大，则继续找他的右子树
        #         node = node.right
        #     return node

    def search_father(self,k): #搜索返回当前值和其父节点
        parent = None
        node = self.root
        while node and node.val != k: #判断是否存在当前值
            parent = node
            if k < node.val:   #如果比当前节点值小，则继续找他的左子树
                node = node.left
            else:               #如果比当前节点值大，则继续找他的右子树
                node = node.right
            return node,parent
    def insert(self,k):
        node,parent = self.search_father(k)
        if node: #如果node不为空，说明已经存在，直接return
            return
        else:
            node = TreeNode(k)
            if parent is None:
                self.root = node
            elif k < parent.data:
                parent.left = node
            else:
                parent.right = node

    def delete(self,k):  #如果删除的不是叶子节点？
        pass



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