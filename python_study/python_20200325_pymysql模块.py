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

# 4：注意：（1）.如果需要返回的数据格式为字典，可使用connect中的cursorclass参数，
#              cursorclass=pymysql.cursors.DictCursor时，fetchone或fetchall 返回的数据均为字典，不再为元祖
#        （2）. 一个连接下，多个cursor查询数据库时，需手动提交事务，才能保证下一次提交查询正确
#              手动提交事务：connect.commit()
#        （3）.查询sql中包含中文，或结果中包含，需添加编码。connect中的charset默认为空字符串。
#              将charset='utf8',即可进行编码。

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
        self.cont.commit()  # 提交事务

        return result


    def fecth_all(self, sql):  # 数据库查询 返回所有数据
        curo = self.cont.cursor()  # 建立游标
        curo.execute(sql)  # 执行sql
        result = curo.fetchall()  # 返回结果数据 元组形式
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

    # 返回元组数据格式
    # my_sql = pymysql.connect(host, user, password, database, port)
    # cursor = my_sql.cursor()
    # cursor.execute(sql)
    # result = cursor.fetchone()  # 返回结果为元组
    # print(result)

    # 返回字典数据格式
    # cont = pymysql.connect(host=host, user=user, password=password, database=database, port=port, cursorclass=pymysql.cursors.DictCursor)
    # cur = cont.cursor()
    # cur.execute(sql)
    # print(cur.fetchone())  # 返回字典数据：{'MobilePhone': '18999999999'}

    # 调用DoMysql函数
    mysql = DoMysql(host, user, password, database, port)
    res = mysql.fecth_one(sql=sql)
    print(res)