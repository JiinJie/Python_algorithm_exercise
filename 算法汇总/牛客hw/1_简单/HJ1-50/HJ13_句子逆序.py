# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 14:39
# @Author  : jinjie
# @File    : HJ13_句子逆序.py

"""
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
"""
temp_list = list(input().split(' '))

str = ''

for i in range(len(temp_list)):
    str  = str+temp_list.pop()+' '

print(str)

