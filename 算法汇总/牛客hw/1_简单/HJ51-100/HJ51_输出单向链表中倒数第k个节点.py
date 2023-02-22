# -*- coding: utf-8 -*-
# @Time    : 2023/2/8 11:01
# @Author  : jinjie
# @File    : HJ51_输出单向链表中倒数第k个节点.py

"""
输入一个单向链表，输出该链表中倒数第k个结点，链表的倒数第1个结点为链表的尾指针。
"""

# 方法一：直接用list实现 双指针
while True:
    try:
        link_len = int(input())
        link_str = list(input().split(' '))
        k = int(input())
        link_str2 = link_str[k-1:]
        for i in range(len(link_str2)):
            #print(i)
            if i == len(link_str2)-1:
                print(link_str[i])
    except:
        break

# 方法二：创建链表
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