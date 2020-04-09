#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : test_register.py
@Date  : 2020/3/24 0024 17:10
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

sheet_name = "register"
file_name = os.path.join(test_data_dir, 'test_case.xlsx')
do_excel = DoExcel(file_name)
cases_data = do_excel.get_case(sheet_name)
conf = DoConf()
sql = 'SELECT * FROM member WHERE MobilePhone !="" ORDER BY MobilePhone DESC LIMIT 1'





@ddt
class TestRegister(TestCase):

    @classmethod
    def setUpClass(cls):
       cls.mysql = DoMysql()

    def setUp(self):
        print("*" * 20 + "用例执行开始" + "*" * 20)
        max_phone = self.mysql.fecth_one(sql)["MobilePhone"]
        phone = str(int(max_phone)+1)
        # 判断数据库取出的手机号是否为非法号段
        pat = '^[1](([3][0-9])|([4][5-9])|([5][0-3,5-9])|([6][5,6])|([7][0-8])|([8][0-9])|([9][1,8,9]))[0-9]{8}$'
        while re.search(pattern=pat, string=phone) is None:
            print("phone不符合手机号码格式为:{}".format(phone))
            phone = str(int(phone)+100000000)
        self.phone = str(phone)


    @data(*cases_data)
    def test_register(self, case):
        if re.search(string=case.params, pattern="\$\{(.*?)\}"):
            params = re.sub(pattern='\$\{(.*?)\}', repl=self.phone, string=case.params)  # repl值需为str
            params = json.loads(params)
            print(params)
        else:
            params = json.loads(case.params)
        print(params)
        url = conf.get_conf_str("api", "url") + case.url
        res = HttpRequest(method=case.method, url=url, params=params)
        actual = res.get_text()
        do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=8, value=actual)
        try:
            self.assertEqual(case.expect, res.get_text())
            result = 'pass'
        except AssertionError as e:
            result = 'fail'
            raise e
        do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)

        add_sql = 'SELECT * FROM member WHERE MobilePhone ={}'.format(self.phone)
        try:
            add_user_msg = self.mysql.fecth_one(add_sql)
            print(add_user_msg)
            # self.assertEqual(add_user_msg[''])
        except Exception as e:
            print("数据库新增用户失败")
            raise e

    def tearDown(self):
        print("*"*20+"用例执行完成"+"*"*20)

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close_connect()



