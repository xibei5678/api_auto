# -*- coding: utf-8 -*-
# @Time : 2020/3/29 20:28
# @Author : xibei
# @filename : do_mysql.py
# @description ：mysql 数据库连接

import pymysql
from python_api_test_qianchendai.common.read_conf import ReadConf



class DoMysql:

    def __init__(self):
        host = ReadConf().get_conf_str("mysql", "host")
        user = ReadConf().get_conf_str("mysql", "user")
        password = ReadConf().get_conf_str("mysql", "password")
        database = ReadConf().get_conf_str("mysql", "database")
        port = ReadConf().get_conf_int("mysql", "port")
        try:
            self.cont = pymysql.connect(host=host, user=user, password=password, database=database, port=port)
        except Exception as e:
            raise e

    def fecth_one(self, sql):  # 返回一条数据
        curo = self.cont.cursor()  # 建立游标
        curo.execute(sql)  # 执行sql
        return curo.fetchone()  # 返回结果数据 元组形式

    def close_connect(self):  # 断开连接
        return self.cont.close()



if __name__ == '__main__':

    sql = 'SELECT * FROM member WHERE MobilePhone !="" ORDER BY MobilePhone DESC LIMIT 1'
    my_sql = DoMysql()
    result = my_sql.fecth_one(sql)
    print(result)