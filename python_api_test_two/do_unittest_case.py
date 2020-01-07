#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : do_unittest_case.py
@Date  : 2020/1/6 0006 15:08
@Author: xibei
'''

from ddt import ddt, data
import unittest
from python_api_test_two.do_conf import DoConf
from python_api_test_two.do_excel import DoExcel
from python_api_test_two.do_logger import DoLog
from python_api_test_two.do_http import DoHttp

conf_value = DoConf('test_environment.conf')
test_data = DoExcel.read_data(conf_value('case', 'file_name'), conf_value('case', 'sheet_name'))
# print(test_data)
my_log = DoLog()

@ddt
class DoUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.http_req = DoHttp()

    @data(*test_data)
    def test_request(self, item):
        url = conf_value('case', 'url')+item['url']
        params = eval(item['params'])
        # 数据检查
        print('****开始进行第{}条用例****'.format(item['case_id']))
        print('用例的标题为：{}'.format(item['title']))
        print('用例的url为：{0}'.format(url))
        print('用例的method为：{}'.format(item['method']))
        print('用例的params为：{}'.format(params))
        print('用例的expect为：{}'.format(item['expect']))
        # 发起请求
        res = self.http_req(method=item['method'], url=url, data=params)
        print('响应结果为：{}'.format(res.json()))
        # 断言
        try:
            self.assertEqual(res.json()['msg'], item['expect'])
        except Exception as e:
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_req.close_request()







