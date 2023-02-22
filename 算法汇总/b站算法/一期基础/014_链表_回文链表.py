# -*- coding: utf-8 -*-
# @Time    : 2023/2/5 18:05
# @Author  : jinjie
# @File    : 014_链表_回文链表.py
"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list2link(List):
    head = ListNode(List[0])#创建一个头节点并将list第一个值赋值给头结点
    p = head#创建头指针
    for i in range(1, len(List)):#list从第二位开始遍历
        p.next = ListNode(List[i])#下一个结点p.next指向list值
        p = p.next#指针往下移动
    return head#返回头结点


# 解法一：基础版  将链表取右半边，然后倒序，遍历与原链表进行对比。出现不一致则不是
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast_p = slow_p = head
        while(fast_p and fast_p.next):
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            if (fast_p):
                slow_p = slow_p.next
            slow_p = self.reverse(slow_p)
            fast_p = head
            while(slow_p and fast_p):
                if(fast_p.val != slow_p.val):
                    return False
                fast_p = fast_p.next
                slow_p = slow_p.next

        return True

    def reverse(self, head: Optional[ListNode]):
        pre_node = None  # pre_node用于存放倒序的链表索引,先置空
        cur_node = head  #p_head 指向head
        while(cur_node):
            temp = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = temp
        return pre_node

# 解法二：精简版
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast_p = slow_p = head
        while(fast_p and fast_p.next):
            fast_p = fast_p.next.next
            slow_p = slow_p.next
        if (fast_p):
            slow_p = slow_p.next
        slow_p = self.reverse(slow_p)
        fast_p = head
        while(slow_p and fast_p):
            if(fast_p.val != slow_p.val):
                return False
            fast_p = fast_p.next
            slow_p = slow_p.next

        return True

    def reverse(self, head: Optional[ListNode]):
        pre_node = None  # pre_node用于存放倒序的链表索引,先置空
        cur_node = head  #p_head 指向head
        while(cur_node):
            temp = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = temp
        return pre_node

# 解法三：直接保存值为栈，然后与原链表对比

class Solution3:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False
        tmp=head
        stack=[]
        while tmp:
            stack.append(tmp.val)
            tmp=tmp.next
        while head:
            if head.val !=stack.pop():
                return False
            head=head.next
        return True


if __name__ == '__main__':
    list = [1,2]
    link1 = list2link(list)
    a = Solution().isPalindrome(link1)

    print(a)
