#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : test_reharge.py
@Date  : 2020/4/13 0013 11:09
@Author: xibei
'''

from unittest import TestCase
from python_api_test_qianchendai.common.do_excel import DoExcel
from python_api_test_qianchendai.common.context import *
from python_api_test_qianchendai.common.do_mysql import DoMysql
from python_api_test_qianchendai.common.http_requets import HttpRequest
from python_api_test_qianchendai.common.read_conf import DoConf
from python_api_test_qianchendai.common.constant import *
import json
from ddt import data, ddt
import re
import os
import time

sheet_name = "recharge"
file_name = os.path.join(test_data_dir, 'test_case.xlsx')
do_excel = DoExcel(file_name)
cases_data = do_excel.get_case(sheet_name)
conf = DoConf()


@ddt
class Recharge(TestCase):

    @classmethod
    def setUpClass(cls):
        global mysql
        mysql = DoMysql()

    def setUp(self):
        print("*" * 20 + "用例执行准备" + "*" * 20)
        sql = 'SELECT LeaveAmount FROM member WHERE MobilePhone ={}'.format(getattr(Context, 'normal_name'))
        self.amount_begin = mysql.fecth_one(sql=sql)['LeaveAmount']
        mysql.close_cursor()
        print("充值前余额:{}".format(self.amount_begin))

    @data(*cases_data)
    def test_recharge(self, case):
        print("*" * 20 + "开始标题为:{}的用例执行".format(case.title) + "*" * 20)
        # 参数检测
        url = conf.get_conf_str("api", "url") + case.url  # 地址拼接
        print("请求地址url为：{}".format(url))
        params = DoRegex().replace(case.params)  # 正则进行替换
        params = json.loads(params)
        print("请求参数params为：{}".format(params))

        # 判断cookies是否存在Context中
        if hasattr(Context, 'cookies'):
            cookies = getattr(Context, 'cookies')
        else:
            cookies = None

        # 查询数据库
        # sql = 'SELECT LeaveAmount FROM member WHERE MobilePhone ={}'.format(getattr(Context, 'normal_name'))
        # amount_begin = mysql.fecth_one(sql=sql)['LeaveAmount']
        # print("充值前余额:{}".format(amount_begin))

        # 发起请求
        res = HttpRequest(method=case.method, url=url, params=params, cookies=cookies)

        # 设置cookies
        if res.get_cookies():
            setattr(Context, "cookies", res.get_cookies())

        # 返回结果 写入excel
        actual = res.get_text()
        do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=8, value=actual)

        # 断言期望值与返回值：状态码
        try:
            self.assertEqual(str(case.expect), res.get_json()['code'])
            result = 'pass'
            do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)
        except AssertionError as e:
            result = 'fail'
            do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)
            raise e

        # 再次查询数据库
        if res.get_json()["msg"] == "充值成功":
            time.sleep(3)
            sql = 'SELECT * FROM member WHERE MobilePhone ={}'.format(params['mobilephone'])
            amount_after = mysql.fecth_one(sql=sql)['LeaveAmount']
            print("充值后余额:{}".format(amount_after))
            try:
                self.assertEqual(float(self.amount_begin)+float(params["amount"]), float(amount_after))
            except AssertionError as e:
                raise e

    def tearDown(self):
        mysql.close_cursor()
        # mysql.close_connect()
        print("*" * 20 + "用例执行结束" + "*" * 20)

    @classmethod
    def tearDownClass(cls):
        mysql.close_connect()



