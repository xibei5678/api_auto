# -*- coding: utf-8 -*-
# @Time : 2020/3/29 20:28
# @Author : xibei
# @filename : do_mysql.py
# @description ：mysql 数据库连接

import pymysql
from python_api_test_qianchendai.common.read_conf import DoConf



class DoMysql:

    def __init__(self):
        host = DoConf().get_conf_str("mysql", "host")
        user = DoConf().get_conf_str("mysql", "user")
        password = DoConf().get_conf_str("mysql", "password")
        database = DoConf().get_conf_str("mysql", "database")
        port = DoConf().get_conf_int("mysql", "port")
        try:
            self.cont = pymysql.connect(host=host, user=user, password=password, database=database, port=port, cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            raise e

    def fecth_one(self, sql):  # 返回一条数据
        self.curo = self.cont.cursor()  # 建立游标
        self.curo.execute(sql)  # 执行sql
        self.cont.commit()  # 手动提交事务
        return self.curo.fetchone()  # 返回结果数据 元组形式

    def close_cursor(self):
        self.curo.close()


    def close_connect(self):  # 断开连接
        return self.cont.close()



if __name__ == '__main__':

    sql = 'SELECT * FROM member WHERE MobilePhone !="" ORDER BY MobilePhone DESC LIMIT 1'
    my_sql = DoMysql()
    result = my_sql.fecth_one(sql)
    print(result)