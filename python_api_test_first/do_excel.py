#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : do_excel.py
@Date  : 2019/12/25 0025 15:56
@Author: xibei
'''

from openpyxl import load_workbook


class DoExcel:

    def do_excel(self, file_name, sheet_name):
        wb = load_workbook(file_name)
        sheet = wb[sheet_name]
        test_case = []
        for i in range(2, sheet.max_row+1):
            single_case = {}
            single_case[sheet.cell(1, 1).value] = sheet.cell(i, 1).value
            single_case[sheet.cell(1, 2).value] = sheet.cell(i, 2).value
            single_case[sheet.cell(1, 3).value] = sheet.cell(i, 3).value
            single_case[sheet.cell(1, 4).value] = sheet.cell(i, 4).value
            single_case[sheet.cell(1, 5).value] = sheet.cell(i, 5).value
            single_case[sheet.cell(1, 6).value] = sheet.cell(i, 6).value

            test_case.append(single_case)

        return test_case


if __name__ == '__main__':
    a = DoExcel()
    for i in a.do_excel('test_case.xlsx', 'Sheet1'):
        print(i)
        print()
