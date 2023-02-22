# -*- coding: utf-8 -*-
# @Time    : 2023/2/5 11:50
# @Author  : jinjie
# @File    : 010_链表_环形链表1.py


"""
给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
如果链表中存在环 ，则返回 true 。 否则，返回 false 。

"""
from typing import Optional
def list2link(List):
    """程序运行需要，与算法无关"""
    head = ListNode(List[0])#创建一个头节点并将list第一个值赋值给头结点
    p = head#创建头指针
    for i in range(1, len(List)):#list从第二位开始遍历
        p.next = ListNode(List[i])#下一个结点p.next指向list值
        p = p.next#指针往下移动
    return head#返回头结点

# 进阶解法 用O(1) 空间复杂度解决
# 方法一： 环形链表 使用 弗洛伊德（floyd）方法解决 【快慢双指针】
# 同时遍历节点，如果快指针和满指针相遇，则说明这是环形链表





# 方法二： hash表，将已经遍历的next放入字典中
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp_dict = {}
        cur = head
        if head == None:
            return False

        while(cur):
            if temp_dict.get(hash(cur.next)):
                return True
            else:
                temp_dict.update({f'{hash(cur.next)}':'anything'})
            cur = cur.next

            return False



if __name__ == '__main__':
    pass




