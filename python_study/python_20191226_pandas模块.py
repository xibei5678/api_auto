#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191226_pandas模块.py
@Date  : 2019/12/26 0026 11:30
@Author: xibei
'''



'''pandas模块'''

# 1. 第三方库，需手动安装：pip install pandas（pandas依赖处理Excel的xlrd模块，在安装之前先安装xlrd模块：pip install xlrd）
# 2. 读取excel数据，pandas 默认把第一行设置为表头，故会从第二行开始读取数据，且索引为0.
# 3. 获取表单数据：
#     1）：pandas.read_excel(file_name,sheet_name) #读取数据，
#       a：sheet_name不输入时，默认读取第一个表单,返回整个表单数据（sheet_data）
#       b：sheet_name 可为表单名、索引（从0开始）
#       c：sheet_name 可为list，获取指定多个表单数据。list中可为表单名或索引
#     2): sheet_data.head(数字)  # 获取前多少行的数据，不适用于多个表单数据
#     3）：sheets_data.values()  # 获取所有数值，应用于多个表单数据的数值获取
#
# 4. 操作行：
#        1): sheet_data.loc[行索引].values  # 操作单行
#        2）：sheet_data.loc[[行索引1,行索引2..]].values  # 操作多行
#        3）：sheet_data.loc[行索引1,列索引2] # 操作指定行列数据（单元格）
#        4）：sheet_data.loc[[row_index_1,row_index_2..],[column_index_1,column_index_2..]] # 操作多行多列数据
#
# 5.操作列：
#       1）：sheet_data['列名'] # 返回list 类字典取值
#       2）：不支持多列取值

# 6.获取列名:sheet_data.columns.values

# 7.获取行索引：sheet_data.index.values

# 6）.数据直接转换成dict
#    sheet_data.loc[row_index,[key1，key2...]].to_dict()




import pandas as pd
import os

base_path = os.path.dirname(os.path.dirname(__file__))  # 获取根目录地址
file_name = os.path.join(base_path, 'python_api_test_first', 'test_case.xlsx')

'''读取表单数据'''

# 方法一：默认取第一个表单
test_data = pd.read_excel(file_name)  # 默认读取第一个表单，返回结果为：矩阵数据

# 方法二：指定表单名
# test_data = pd.read_excel(file_name, sheet_name='Sheet2')


# 方法三：通过索引进去获取
# test_data = pd.read_excel(file_name, sheet_name=0)

# 方法四：通过索引获取多个表单
# test_data = pd.read_excel(file_name, sheet_name=[0, 1])

# 方法五：通过表单名获取多个表单
# test_data = pd.read_excel(file_name, sheet_name=['Sheet1', 'Sheet2'])

# print(test_data)
# print(test_data.head(2))  # 获取前两行的数据，适用于方法一二三，不适用方法四、五
# print(test_data.values())   # 适用方法四、五，不适用于方法一二三，返回所有表单的二维矩阵数组



'''操作行列'''


# 获取单行数据
# row_data = test_data.loc[0].values

# 获取多行数据
# row_data = test_data.loc[[0, 1, 2]].values  # 返回嵌套的list数据

# 获取指定行列数据（单元格数据）
# row_data = test_data.iloc[0, 1]

# 获取指定多行多列数据
# row_data = test_data.iloc[[0, 1], [2, 3]].values  # 返回嵌套list

# print(row_data)

# 获取指定列
column_data = test_data['case_id']
# column_data = test_data['case_id', 'method']  # 错误示例，只能单列取值
# print(column_data)

# 获取列名并打印输出
column_title = test_data.columns.values
# print(column_title)

# 获取行号索引
row_index = test_data.index.values  # 返回行号索引的list
# print(row_index)



'''将数据转为dict'''

row_data_dict = test_data.loc[0, column_title].to_dict()   # 注意获取单行的数据，单行数据个数需与key个数一样多
# print(row_data_dict)

# list_data = []
# for i in row_index:  # 遍历每一行 row_index 行号索引list
#     dict_data = test_data.loc[i, column_title].to_dict()  # column_title 表头
#     list_data.append(dict_data)
# print(list_data)