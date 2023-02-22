# -*- coding: utf-8 -*-
# @Time    : 2023/2/5 15:39
# @Author  : jinjie
# @File    : 012_链表_相交链表.py

"""
给你两个单链表的头节点 headA 和 headB ，
请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

"""
# 解析：
"""
我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
第二个指针 cur 指向 head，然后不断遍历 cur。
每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==None or headB==None:
            return None
        p_a = headA
        p_b = headB
        while(p_a != p_b):
            if p_a == None:
                p_a = headB    #指向head节点而不是next
            p_a = p_a.next
            if p_b == None:
                p_b = headA
            p_b = p_b.next
        return p_a

