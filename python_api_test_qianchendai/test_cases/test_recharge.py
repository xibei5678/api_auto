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

sheet_name = "recharge"
file_name = os.path.join(test_data_dir, 'test_case.xlsx')
do_excel = DoExcel(file_name)
cases_data = do_excel.get_case(sheet_name)
conf = DoConf()

patter = "\$\{(.*?)\}"
# cookies = None


@ddt
class Recharge(TestCase):

    def setUp(self):
        self.mysql = DoMysql()
        print("*" * 20 + "用例执行准备" + "*" * 20)

    @data(*cases_data)
    def test_recharge(self, case):
        print("*" * 20 + "{}用例执行开始".format(case.title) + "*" * 20)
        url = conf.get_conf_str("api", "url") + case.url
        print("url为：{}".format(url))
        if re.search(pattern=patter, string=case.params):
            params = DoRegex().replace(case.params)
            params = json.loads(params)
        else:
            params = json.loads(case.params)
        print("params：{}".format(params))
        if hasattr(Context, 'cookies'):
            cookies = getattr(Context, 'cookies')
        else:
            cookies = None
        sql = 'SELECT LeaveAmount FROM member WHERE MobilePhone ={}'.format(params['mobilephone'])
        if self.mysql.fecth_one(sql=sql):
            leavemount_1 = int(self.mysql.fecth_one(sql=sql)['LeaveAmount'])
            # self.mysql.close_cursor()
        else:
            leavemount_1 = None
        print("充值前余额:{}".format(leavemount_1))
        res = HttpRequest(method=case.method, url=url, params=params, cookies=cookies)

        if res.get_cookies():
            setattr(Context, "cookies", res.get_cookies())
        actual = res.get_text()
        do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=8, value=actual)
        try:
            self.assertEqual(str(case.expect), res.get_json()['code'])
            result = 'pass'
            do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)
        except AssertionError as e:
            result = 'fail'
            do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)
            raise e

        if self.mysql.fecth_one(sql=sql):
            leavemount_2 = int(self.mysql.fecth_one(sql=sql)['LeaveAmount'])
            # self.mysql.close_cursor()
        else:
            leavemount_2 = None

        print("充值金额:{}".format(params['amount']))
        print("充值后余额:{}".format(leavemount_2))

        if res.get_json()["msg"] == "充值成功":
            # print(params['amount'])
            if leavemount_2 == leavemount_1+int(params['amount']):
                print("数据库余额验证成功")
            else:
                print("数据库余额验证失败")
        else:
            if leavemount_2 == leavemount_1:
                print("数据库余额验证成功")
            else:
                print("数据库余额验证失败")


    def tearDown(self):
        # self.mysql.close_cursor()
        self.mysql.close_connect()
        print("*" * 20 + "用例执行结束" + "*" * 20)



