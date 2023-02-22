# -*- coding: utf-8 -*-
# @Time    : 2023/2/3 16:45
# @Author  : jinjie
# @File    : ms_009_遍历文件.py
# 遍历某个文件夹下的所有文件，并筛选出指定后缀内容

import os
from pathlib import Path
from pprint import pprint

# 获取当前位置
current_path = os.path.realpath(__file__)
# 通过Path对象获取当前文件所在文件夹的路径
current_dir = Path(current_path).parent


myrule = '.py'


def get_files(path,rule):
    print(path)
    all = []
    for fpath,dirs,files in os.walk(path):
        # dirs为空表示当前文件夹下没有子文件夹
        #print(fpath,dirs,files)
        for f in files:
            filename = os.path.join(fpath,f)
            if filename.endswith(rule):
                all.append(filename)
    return all


if __name__ == '__main__':
    all_file_path = get_files(current_dir,myrule)
    pprint(all_file_path)