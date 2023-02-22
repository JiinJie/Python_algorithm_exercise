# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 10:39
# @Author  : jinjie
# @File    : 017_栈与队列_用栈实现队列.py
"""
请你仅使用两个栈实现先入先出队列。
队列应当支持一般队列支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false

"""


class MyQueue:

    def __init__(self):
        # in负责push操作 ,out负责pop操作
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()  # 先pop out已有的数据

        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        # 由于该题要求先进先出。那队列头即为最后一个进入的值
        # 即 stack_in = [:-1]
        head = self.pop()
        self.stack_out.append(head)
        return head

    def empty(self) -> bool:
        if self.stack_in or self.stack_out:
            return False
        else:
            return True

if __name__ == '__main__':
    obj = MyQueue()
    x = [[],[1],[2],[],[],[]]
    obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    print(param_2,param_3,param_4)