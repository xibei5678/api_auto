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
#         d.执行sql
#         e.返回结果


import pymysql



class DoMysql:

    def __init__(self, host, user, password, database, port):
        try:
            self.cont = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
        except Exception as e:
            raise e

    def fecth_one(self, sql):  # 数据库查询 返回一条数据
        curo = self.cont.cursor()  # 建立游标
        curo.execute(sql)  # 执行sql
        result = curo.fetchone()  # 返回结果数据 元组形式
        curo.close()  # 关闭游标
        return result


    def fecth_all(self, sql):  # 数据库查询 返回所有数据
        curo = self.cont.cursor()  # 建立游标
        curo.execute(sql)  # 执行sql
        result = curo.fetchall()  # 返回结果数据 元组形式
        curo.close()
        return result

    # def fecth_many(self, sql, size):  # 数据库查询 返回多条数据 size:返回条数
    #         curo = self.cont.cursor()  # 建立游标
    #         curo.execute(sql)  # 执行sql
    #         return curo.fetchmany(sql, size=size)  # 返回结果数据 元组形式

    def db_close(self):
        return self.cont.close()  # 关闭数据连接

if __name__ == '__main__':

    host = "test.lemonban.com"
    user = "test"
    password = "test"
    database = "future"
    port = 3306
    sql = 'SELECT MobilePhone FROM member WHERE MobilePhone !="" ORDER BY MobilePhone DESC LIMIT 10'
    # my_sql = pymysql.connect(host, user, password, database, port)
    # cursor = my_sql.cursor()
    # cursor.execute(sql)
    # result = cursor.fetchone()  # 返回结果为元组
    # print(result)
    mysql = DoMysql(host, user, password, database, port)
    res = mysql.fecth_all(sql=sql)
    print(res)