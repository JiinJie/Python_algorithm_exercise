# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 13:39
# @Author  : jinjie
# @File    : 008_单词接龙_100.py

"""
题目
单词接龙的规则是：
可用于接龙的单词，首字母必须要与前一个单词的尾字母相同；
当存在多个首字母相同的单词时，取长度最长的单词；
如果长度也相等，则取字典序最小的单词；
已经参与接龙的单词不能重复使用；
现给定一组全部由小写字母纟且成的单词数组，
并指定其中一个单词为起始单词，进行单词接龙，
请输出最长的单词串。
单词串是单词拼接而成的，中间没有空格。
单词个数1<N<20
单个单词的长度1～30
"""

# 解法一
start_index = int(input())
nums = int(input())
str_list = []

res = ""

for _ in range(nums):
    str_list.append(input())

res = str(str_list.pop(start_index))
sort_list = sorted(str_list,key=lambda str_list:(-len(str_list),str_list))

#print(sort_list)

for i in sort_list:
    end_char = res[-1]
    if i.startswith(end_char):
        res += str(i)
        sort_list.remove(i)

print(res)


# 解法二：offical
def solve(k, words):
    builder = words[k]
    del words[k]

    words = sorted(words, key=lambda x: (-len(x), x))

    while True:
        len_ = len(builder)
        last = builder[-1]
        for i in range(len(words)):
            cur = words[i]
            if cur.startswith(last):
                builder += cur
                del words[i]
                break
        if len(builder) == len_:
            break

    return builder


if __name__ == '__main__':

    k = int(input())
    N = int(input())
    words = []
    for i in range(N):
        words.append(input().strip())

    result = solve(k, words)
    print(result)

