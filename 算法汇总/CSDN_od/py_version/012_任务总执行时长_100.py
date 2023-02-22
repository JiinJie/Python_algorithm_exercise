# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 17:19
# @Author  : jinjie
# @File    : 012_任务总执行时长_100.py

"""
题目
任务编排服务负责对任务进行组合调度。
参与编排的任务又两种类型，
其中一种执行时长为taskA，
另一种执行时长为taskB。
任务一旦开始执行不能被打断，且任务可连续执行。
服务每次可以编排num个任务。
请编写一个方法，生成每次编排后的任务所有可能的总执行时长。
"""

str_in = list(map(int,input().split(",")))
#print(str_in)
taska_t = str_in[0]
taskb_t = str_in[1]
task_times = int(str_in[2])
temp_list = []

for i in range(task_times+1):
    sum = taska_t*i + taskb_t*(task_times-i)
    temp_list.append(sum)


print(sorted(temp_list))
