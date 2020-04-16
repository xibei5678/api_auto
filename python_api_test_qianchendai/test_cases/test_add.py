#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : test_add.py
@Date  : 2020/4/15 0015 16:35
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
import datetime
import random

sheet_name = "add"
file_name = os.path.join(test_data_dir, 'test_case.xlsx')
do_excel = DoExcel(file_name)
cases_data = do_excel.get_case(sheet_name)
conf = DoConf()


@ddt
class TestAdd(TestCase):

    def setUp(self):
        print("*" * 20 + "用例执行准备" + "*" * 20)

    def tearDown(self):
        print("*" * 20 + "测试结束" + "*" * 20)

    @data(*cases_data)
    def test_add(self, case):

        # 参数检查
        url = conf.get_conf_str("api", "url") + case.url
        print("请求地址url：{}".format(url))
        params = DoRegex.replace(case.params)
        params = json.loads(params)
        # try:
        #     if params['title']:
        #         conf.write_conf("regex", "title", conf.get_conf_str("regex", "title") + "_{}".format(range(0, 1000)))
        # except KeyError as e:
        #     pass
        print("请求参数params：{}".format(params))

        # 判断cookies是否存在Context中
        if hasattr(Context, 'cookies'):
            cookies = getattr(Context, 'cookies')
        else:
            cookies = None

        #

