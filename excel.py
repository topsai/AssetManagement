#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import xdrlib, sys
import xlrd

file = 'C:/Users/john/Desktop/1.xlsx'


def open_excel(f):
    try:
        data = xlrd.open_workbook(f)
        return data
    except Exception as e:
        print(e)

data = open_excel(file)
table = data.sheets()[0]  # 通过索引顺序获取
print(table.row_values(0))
print(table.col_values(0))