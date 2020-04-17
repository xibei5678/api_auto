#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : test_audit.py
@Date  : 2020/4/17 0017 16:27
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
import random


sheet_name = "audit"
file_name = os.path.join(test_data_dir, 'test_case.xlsx')
do_excel = DoExcel(file_name)
cases_data = do_excel.get_case(sheet_name)
conf = DoConf()


@ddt
class TestAudit(TestCase):

    @classmethod
    def setUpClass(cls):
        global mysql
        mysql = DoMysql()

    @classmethod
    def tearDownClass(cls):
        mysql.close_connect()

    def setUp(self):
        print("*" * 20 + "用例执行准备" + "*" * 20)

        # 查询配置文件中的标名是否已存在，存在：更改标名再查询
        sql = "SELECT * FROM loan WHERE Title='{}'".format(conf.get_conf_str("regex", "title"))
        mysql_result = mysql.fecth_one(sql=sql)
        # 如果存在，在标名后加入随机数，存入到Context中以用于替换
        while mysql_result:
            title_value = conf.get_conf_str("regex", "title") + "_{0}".format(random.randint(0, 1000))
            setattr(Context, 'title', title_value)
            sql = "SELECT * FROM loan WHERE Title='{}'".format(getattr(Context, 'title'))
            mysql_result = mysql.fecth_one(sql=sql)
        # loan_id = mysql_result['id']
        # setattr(Context, 'id', loan_id)


    def tearDown(self):
        print("*" * 20 + "测试结束" + "*" * 20)

    @data(*cases_data)
    def test_add(self, case):
        # 参数检查
        url = conf.get_conf_str("api", "url") + case.url
        print("请求地址url：{}".format(url))

        # 请求参数处理
        # if int(json.loads(case.params)['status']) >= 8:
        #     status = json.loads(case.params)['status']
        #     sql = "SELECT * FROM loan WHERE Status='{}'".format(status)
        #     mysql_result = mysql.fecth_one(sql=sql)
        #     loan_id = str(mysql_result['Id'])
        #     setattr(Context, 'loan_id', loan_id)
        #     params = DoRegex.replace(case.params)
        #     params = json.loads(params)
        #     params['status'] = int(status)-1

        params = DoRegex.replace(case.params)
        params = json.loads(params)
        print("请求参数params：{}".format(params))



        # 判断cookies是否存在Context中
        if hasattr(Context, 'cookies'):
            cookies = getattr(Context, 'cookies')
        else:
            cookies = None

        # 发起请求
        res = HttpRequest(method=case.method, url=url, params=params, cookies=cookies)

        # cookies 保存
        if res.get_cookies():
            setattr(Context, "cookies", res.get_cookies())

        # 加标后，将标id存入Context中，用于替换
        if res.get_json()["msg"] == "加标成功":
            sql = "SELECT * FROM loan WHERE Title='{}'".format(params['title'])
            mysql_result = mysql.fecth_one(sql=sql)
            loan_id = str(mysql_result['Id'])
            setattr(Context, 'loan_id', loan_id)

        # 返回结果 写入excel
        actual = res.get_text()
        do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=8, value=actual)
        print(actual)
