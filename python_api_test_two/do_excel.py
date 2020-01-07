#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : do_excel.py
@Date  : 2020/1/6 0006 15:05
@Author: xibei
'''

import pandas

class DoExcel:

    @staticmethod
    def read_data(file_name, sheet_name=0):
        # 获取指定表单数据
        test_data = pandas.read_excel(file_name, sheet_name)
        # 获取表头
        column_title = test_data.columns.values

        # 获取所有行索引
        row_index = test_data.index.values

        cases_data = []
        # 遍历每行数据，每行数据存储为字典形式
        for i in row_index:
            row_case = test_data.loc[i, column_title].to_dict()
            cases_data.append(row_case)

        return cases_data



if __name__ == '__main__':

    a = DoExcel.read_data(R'D:\test\python_12_xibei\python_api_test_first\test_case.xlsx')
    print(a)


