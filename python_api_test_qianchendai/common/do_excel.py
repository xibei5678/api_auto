#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : do_excel.py
@Date  : 2020/1/17 0017 10:42
@Author: xibei
'''


from openpyxl import load_workbook


class Case:

    def __init__(self):
        self.id = 1
        self.url = 2
        self.method = 3
        self.title = 4
        self.params = 5
        self.expect = 6


class DoExcel:

    def __init__(self, file_name):
        try:
            self.wb = load_workbook(filename=file_name)
        except FileNotFoundError as e:
            print("{0} not found,pleas check file path".format(file_name))
            raise e

    def get_case(self, sheet_name=None):
        if sheet_name:
            sheet = self.wb[sheet_name]
        else:
            sheet_name = self.wb.sheetnames[0]  # 如果未传入表单，默认读取第一个表单
            sheet = self.wb[sheet_name]
        max_row = sheet.max_row  # 获取最大行
        case_data = []  # 收集所有的用例
        for r in range(2, max_row+1):  # openpyxl 读取excel的索引从1开始，第一行为标题 故从第二行开始读取
            case = Case()  # 实例一个Case ，存储每一行的每条用例
            case.id = sheet.cell(row=r, column=case.id).value
            case.url = sheet.cell(row=r, column=case.url).value
            case.method = sheet.cell(row=r, column=case.method).value
            case.title = sheet.cell(row=r, column=case.title).value
            case.params = sheet.cell(row=r, column=case.params).value
            case.expect = sheet.cell(row=r, column=case.expect).value
            case_data.append(case)

        return case_data



if __name__ == '__main__':

    wb = DoExcel(r"D:\test\python_12_xibei\python_api_test_qianchendai\test_data\cases .xlsx")
    case_data = wb.get_case('login')
    for case in case_data:
        # print(case.id)
        # print(case.url)
        # print(case.method)
        # print(case.params)
        # print(case.expect)
        print(case.__dict__)
