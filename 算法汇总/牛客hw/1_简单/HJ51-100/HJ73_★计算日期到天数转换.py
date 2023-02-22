# -*- coding: utf-8 -*-
# @Time    : 2023/2/9 16:48
# @Author  : jinjie
# @File    : HJ73_★计算日期到天数转换.py

"""
根据输入的日期，计算是这一年的第几天。
保证年份为4位数且日期合法。
进阶：时间复杂度： O(n) ，空间复杂度：O(1)
"""
"""
输入：2012 12 31
输出：366
"""
# 直接使用内置的datetime函数即可
from datetime import datetime

str_in = input().split()
year,month,day = int(str_in[0]),int(str_in[1]),int(str_in[2])
now_date = datetime(year,month,day)
day_sum = now_date.strftime('%j')  # %j将日期转换为天数
print(now_date)

#print(int(day_sum))

"""
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
"""