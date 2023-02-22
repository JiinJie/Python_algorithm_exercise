# -*- coding: utf-8 -*-
# @Time    : 2023/2/5 22:51
# @Author  : jinjie
# @File    : 016_链表_链表中倒数第k个节点.py
"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list2link(List):
    head = ListNode(List[0])#创建一个头节点并将list第一个值赋值给头结点
    p = head#创建头指针
    for i in range(1, len(List)):#list从第二位开始遍历
        p.next = ListNode(List[i])#下一个结点p.next指向list值
        p = p.next#指针往下移动
    return head#返回头结点

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        fast_p = slow_p = head
        for i in range(k):
            # if (fast_p):  #可以省略
                fast_p = fast_p.next
        while(fast_p):
            fast_p = fast_p.next
            slow_p = slow_p.next
        return slow_p


if __name__ == '__main__':
    list = [1,2,3,4,5]
    link1 = list2link(list)
    a = Solution().getKthFromEnd(link1,2)
    while a:
        print(a.val)
        a = a.next
