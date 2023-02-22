# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 21:22
# @Author  : jinjie
# @File    : HJ29_字符串加解密.py
"""
对输入的字符串进行加解密，并输出。

加密方法为：
当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；
字母Z时则替换为a；
当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；
其他字符不做变化。

解密方法为加密的逆过程。
数据范围：输入的两个字符串长度满足
1≤n≤1000  ，保证输入的字符串都是只由大小写字母或者数字组成
"""

"""
输入描述：
第一行输入一串要加密的密码
第二行输入一串加过密的密码

输出描述：
第一行输出加密后的字符
第二行输出解密后的字符
"""

# 方法一：直接映射
def check(a, b):
    L1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    L2 = "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza1234567890"
    result = ""
    if b == 1:
        for i in a:
            result += L2[L1.index(i)]
    elif b == -1:
        for i in a:
            result += L1[L2.index(i)]
    return result


while True:
    try:
        print(check(input(), 1))
        print(check(input(), -1))

    except:
        break


# 方法二：变换
def my_encode(org_str):
    org_str = str(org_str)
    enc_str = ""
    for i in org_str:
        if i == "Z":
            enc_str += 'a'
        elif i == "z":
            enc_str += 'A'
        elif i.islower():
            enc_str += chr(ord(i.upper())+1)
        elif i.isupper():
            enc_str += chr(ord(i.lower())+1)
        elif i.isdigit():
            enc_str += str((int(i)+1)%10)
        else:
            enc_str += i
    return enc_str

def my_decode(enc_str):
    enc_str = str(enc_str)
    org_str = ''
    for i in enc_str:
        if i == "a":
            org_str += 'Z'
        elif i == 'A':
            org_str += 'z'
        elif i.islower():
            org_str += chr(ord(i.upper())-1)
        elif i.isupper():
            org_str += chr(ord(i.lower())-1)
        elif i.isdigit():
            org_str += str((int(i)+9)%10)
        else:
            org_str += i
    return org_str

org_str = input()
enc_str = input()

print(my_encode(org_str=org_str))
print(my_decode(enc_str=enc_str))
