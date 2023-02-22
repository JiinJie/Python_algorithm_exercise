# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 15:00
# @Author  : jinjie
# @File    : 020_二叉树_★三种遍历.py

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
# 创建二叉树 root
root = list_to_binarytree(list_tree)


# 前序遍历：迭代形式
def preorder(root,res=[]):
    if not root:
        return
    res.append(root.val)
    preorder(root.left,res)
    preorder(root.right,res)
    return res

def inorder(root,res=[]):
  if not root:
    return
  inorder(root.left,res)
  res.append(root.val)
  inorder(root.right,res)
  return res

def lastorder(root,res=[]):
  if not root:
    return
  lastorder(root.left,res)
  lastorder(root.right,res)
  res.append(root.val)
  return res


# 输出前序遍历
pre_res = preorder(root,res=[])
print(pre_res)

#输出中序遍历
in_res = inorder(root,res=[])
print(in_res)

# 输出后序遍历
last_res = lastorder(root,res=[])
print(last_res)
