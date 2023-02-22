# -*- coding: utf-8 -*-
# @Time    : 2023/2/4 17:56
# @Author  : jinjie
# @File    : 007_链表_合并两个有序链表.py


from typing import Optional
# Optional是个可选参数


def list2link(List):
    head = ListNode(List[0])#创建一个头节点并将list第一个值赋值给头结点
    p = head#创建头指针
    for i in range(1, len(List)):#list从第二位开始遍历
        p.next = ListNode(List[i])#下一个结点p.next指向list值
        p = p.next#指针往下移动
    return head#返回头结点


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 方法一：递归
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2




# 方法二：循环+双指针 【有报错】
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list_p = ListNode()

        if (list1 == None):
            return list2
        if (list2 == None):
            return list1
        while list1 and list2:
            # 判断大小，小的挂载在P后
            print(list1.val,list2.val)
            if(list1.val <list2.val):
                list_p.next = list1.val
                list1 = list1.next  #指向下一个节点
            else:
                list_p.next = list2.val
                list2 = list2.next

        #list_p = list_p.next
        # 将剩余列表直接挂载在后面
        if list1:
            list_p.next = list1
        if list2:
            list_p.next = list2

        return list_p



if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4]
    link1 = list2link(l1)
    link2 = list2link(l2)
    print(type(link1))
    a = Solution2().mergeTwoLists(link1,link2)
    print(a)
