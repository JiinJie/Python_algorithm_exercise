# -*- coding: utf-8 -*-
# @Time    : 2023/2/5 9:35
# @Author  : jinjie
# @File    : 009_链表_删除排序链表中的重复元素.py

"""
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""

# 解析
"""
★解析cur和head的含义
head本身是链表的第一个对象，含有两个属性，一个是value，表示他的值。一个是next指向下一个对象。
将head赋给cur，此时cur表示的是当前对象。在操作cur时，cur的next发生变化，由于head只存储next的对象地址，因此cur对象的next的值发生变化时，head指向的也是同一个对象，则next的值也会发生变化。
遍历cur后，next被过滤。head指向的next也会过滤
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


#Definition for singly-linked list.

# 解法一：遍历链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
            print(f"cur的值{cur.val}")
            print(f"head的值{head.val}")
            print("-"*10)
        return head,cur

# 解法二：递归解决
class Solution2:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head ==None or head.next==None):
            return head
        head.next = Solution2.deleteDuplicates(self,head.next)
        #return head.val == head.next.val?head.next:head
        """pyhon中的三元运算"""
        return head.next if head.val == head.next.val else head


if __name__ == '__main__':
    head1 = [1, 1, 2]
    head2 = [1, 1, 2, 3, 3]
    link = list2link(head2)
    #head,cur = Solution().deleteDuplicates(link)
    head = Solution2().deleteDuplicates(link)

    while head:  # head中是处理后的值
        print(head.val)
        head = head.next
    print("+"*10)
    while cur: # cur中 只有3
        print(cur.val)
        cur = cur.next


