# -*- coding: utf-8 -*-
# @Time    : 2023/2/5 22:14
# @Author  : jinjie
# @File    : 015_链表_链表的中间节点.py

"""
给定一个头结点为 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
"""


# 解析：
# 快慢双指针 快指针结束时，满指针在中点，
# 若为偶数项则直接获取下一个节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_p = slow_p = head
        while(fast_p.next and fast_p.next.next):
            fast_p = fast_p.next.next
            slow_p = slow_p.next
        if fast_p.next:
            slow_p = slow_p.next
        return slow_p