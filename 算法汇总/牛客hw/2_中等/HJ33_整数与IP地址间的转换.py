# -*- coding: utf-8 -*-
# @Time    : 2023/2/12 10:32
# @Author  : jinjie
# @File    : HJ33_整数与IP地址间的转换.py

"""
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成
一个长整数。
举例：一个ip地址为10.0.3.193
每段数字             相对应的二进制数
10                   00001010
0                    00000000
3                    00000011
193                  11000001
组合起来即为：00001010 00000000 00000011 11000001,转换为10进制数就是：167773121，即该IP地址转换后的数字就是它了。
数据范围：保证输入的是合法的 IP 序列

"""
def encode_ip(str_in):
    str_encode = ""
    # print(str_in)
    for i in str_in:
        str_encode += "{:0>8d}".format(int(bin(int(i))[2:]))  #补足8位整数位
    str_encode = int(str_encode, 2)
    return str_encode


def decode_ip(str_in):
    res = []
    str_decode = "{:0>32d}".format(int(bin(str_in)[2:]))
    for i in range(0, len(str_decode), 8):
        res.append(str(int(str_decode[i:i + 8], 2)))
    str_ip = '.'.join(res)
    # print(str_ip)
    return str_ip


str_in = input().split('.')
str_int = int(input())

print(encode_ip(str_in))
print(decode_ip(str_int))