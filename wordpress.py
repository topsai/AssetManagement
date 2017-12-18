#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

# print(sys.argv, type(sys.argv))
# file = 'C:/Users/john/Desktop/test/index.php'
# p = 'C:/Users/john/Desktop/Roy_Ascott'
file_list = []
kill_files = []
e_list = ['sql', 'py', ]  # 不查杀的文件
num = 0


def list_path(p):
    paths = os.listdir(p)
    for i in paths:
        tmp_dir = os.path.join(p, i)
        if os.path.isfile(tmp_dir):
            file_list.append(tmp_dir)
        else:
            # print(tmp_dir, '-dir')
            list_path(tmp_dir)


list_path(sys.argv[1])

# print(file_list)
# print(len(file_list))

import subprocess


# def rep_url(file, encode):
#     if file.endswith('php'):
#         # print('扫描：', file)
#         with open(file, 'r', encoding=encode) as f:
#
def scans(file, encode):
    if file.endswith('php'):
        # print('扫描：', file)
        with open(file, 'r', encoding=encode) as f:
            #
            a = f.read(10)
            if a == '<?php $smu':
                # 先杀毒
                # print('yes')
                f.seek(7773, 0)
                new_file = f.read()
                # new_file = new_file.replace('http://www.detaoma.com/', '/')
                # print(new_file)
                f.close()
                with open(file, 'w', encoding=encode) as f1:
                    f1.write(new_file)
                    kill_files.append(file)
    for x in e_list:
        if file.endswith(x):
            return
    with open(file, 'r', encoding=encode) as f:
        # 替换字符串
        f.seek(0)
        new_file = f.read()
        if 'http://www.detaoma.com' in new_file:
            print('find detaoma', file)
            assert 's'
            new_file = new_file.replace('http://www.detaoma.com/', '/')
            with open(file, 'w', encoding=encode) as f1:
                f1.write(new_file)
                kill_files.append(file)


import time

for i in file_list:
    try:
        scans(i, 'utf8')
    except Exception as e:
        try:
            scans(i, 'iso-8859-1')
        except:
            print('o m g')

print(kill_files)
print('共计', len(file_list), '个文件，', '查杀', len(kill_files), '个')
