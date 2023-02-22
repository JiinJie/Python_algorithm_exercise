# -*- coding: utf-8 -*-
# @Time    : 2023/2/5 10:20
# @Author  : jinjie
# @File    : 008_链表_★实现列表转链表.py
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

if __name__ == "__main__":
    old_list = [1, 2, 3, 4, 5]
    link = list2link(old_list)
    while link:
        print(link.val ,link.next)
        # next指向的是下一个节点的对象，如果是最后一个，则下一个指向None
        # val 获取的是当前节点的值
        link = link.next

"""输出内容
1 <__main__.ListNode object at 0x00000136910BC0A0>
2 <__main__.ListNode object at 0x00000136910BC670>
3 <__main__.ListNode object at 0x00000136910E9DC0>
4 <__main__.ListNode object at 0x00000136910E9E20>
5 None
"""

