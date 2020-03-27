#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20200325_pymysql模块.py
@Date  : 2020/3/25 0025 14:40
@Author: xibei
'''

'''pymysql模块'''

# 1. 用于数据的查询
# 2. 安装：pip install pymysql
# 3. 操作：
#         a.创建连接（连接成功与否）
#         b.准备sql语句
#         c.连接成功--建立游标
#         d.执行
#         e.返回结果


import pymysql

host="test.lemonban.com"
user="test"
password="test"
database=None
port=3306

class DoMysql:

    def __init__(self):
        try:
            cont = pymysql.connect(host, user, password, database, port)
        except Exception as e:
