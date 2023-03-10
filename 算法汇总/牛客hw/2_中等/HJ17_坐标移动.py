# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 16:30
# @Author  : jinjie
# @File    : HJ17_坐标移动.py

"""
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
"""
"""
处理过程：
起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)
结果 （10， -10）
"""

str_in = list(input().split(";"))

x,y = 0,0

for i in str_in:
    i_direct = i[:1]
    i_step = i[1:]
    #print(i_direct,i_step)
    if i_step.isdigit():
        i_step = int(i_step)
        if i_direct == "A":
            x -= i_step
        elif i_direct == "D":
            x += i_step
        elif i_direct == "W":
            y += i_step
        elif i_direct == "S":
            y -= i_step
    else:
        continue

print(f"{x},{y}")