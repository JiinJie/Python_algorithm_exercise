# -*- coding: utf-8 -*-
# @Time    : 2023/2/5 18:07
# @Author  : jinjie
# @File    : 013_链表_反转链表.py

"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""

"""解析：
我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
第二个指针 cur 指向 head，然后不断遍历 cur。
每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。
"""
# 方法一 双指针迭代获取

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = None  # pre_node用于存放倒序的链表索引,先置空
        cur_node = head  #p_head 指向head
        while(cur_node):
            temp = cur_node.next  # 先将当前节点的下一个节点保存为temp对象
            cur_node.next = pre_node # 将当前节点的下一个节点指向pre_node，即cur_node的前一个元素
            pre_node = cur_node # pre_node指向当前节点,可得出 pre_node.next指向的是cur_node前一个元素
            cur_node = temp  # cur_node 指向下一个节点，继续遍历
        return pre_node  #返回倒序的链表


# 方法二 利用外部空间 不推荐
