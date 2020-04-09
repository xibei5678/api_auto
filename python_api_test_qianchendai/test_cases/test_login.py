#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : test_login.py
@Date  : 2020/3/24 0024 17:16
@Author: xibei
'''


from unittest import TestCase

from python_api_test_qianchendai.common.http_requets import HttpRequest
import json
from python_api_test_qianchendai.common.read_conf import DoConf
from python_api_test_qianchendai.common.do_excel import DoExcel
from ddt import ddt, data, unpack

wb = DoExcel(r"C:\Users\Administrator\Desktop\cases .xlsx")
sheet_name = 'login'
case_data = wb.get_case(sheet_name)
read_conf = DoConf()  # 创建实例 读取测试环境配置文件中的url

@ddt
class TestLogin(TestCase):

    def setUp(self):
        print("*****"*10+"进入测试"+"*****"*10)

    @data(*case_data)
    def test_login(self, case):
        url = read_conf.get_conf_str("api", "url") + case.url
        params = json.loads(case.params)  # excel 获取的数据都是str，故需转化成字典
        resp = HttpRequest(method=case.method, url=url, params=params)
        print("输入的case_id为{}".format(case.id))
        wb.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=7, value=resp.get_text())
        try:
            self.assertEqual(resp.get_json(), json.loads(case.expect))
            wb.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=8, value="pass")
        except AssertionError as e:
            print("期望结果为：{}".format(case.expect))
            print("实际返回结果为：{}".format(resp.get_json()))
            wb.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=8, value="false")
            raise e

    def tearDown(self):
        print("*****" * 10 + "测试结束" + "*****" * 10)