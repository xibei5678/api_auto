#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : test_bidloan.py
@Date  : 2020/4/28 0028 15:24
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
import time

sheet_name = "bidLoan"
file_name = os.path.join(test_data_dir, 'test_case.xlsx')
do_excel = DoExcel(file_name)
cases_data = do_excel.get_case(sheet_name)
conf = DoConf()


@ddt
class TestBidLoan(TestCase):

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
        self.sql_amount = 'SELECT LeaveAmount FROM member WHERE MobilePhone ={}'.format(conf.get_conf_str("regex", 'normal_name'))
        self.amount_start = float(mysql.fecth_one(self.sql_amount)['LeaveAmount'])

    def tearDown(self):
        print("*" * 20 + "测试结束" + "*" * 20)

    @data(*cases_data)
    def test_add(self, case):

        # 参数检查
        url = conf.get_conf_str("api", "url") + case.url
        print("请求地址url：{}".format(url))
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

        # 查询标id
        if res.get_json()['msg'] == '加标成功':
            sql = "SELECT * FROM loan WHERE Title='{}'".format(params['title'])
            sql_result = mysql.fecth_one(sql=sql)
            setattr(Context, "loan_id", str(sql_result['Id']))

        # 返回结果 写入excel
        actual = res.get_text()
        do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=8, value=actual)

        # 断言期望值与返回值：状态码
        try:
            self.assertEqual(case.expect, res.get_text())
            result = 'pass'
            do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)
        except AssertionError as e:
            result = 'fail'
            do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)
            raise e

        if res.get_json()['msg'] == '竞标成功':
            amount_after = float(mysql.fecth_one(self.sql_amount)['LeaveAmount'])
            try:
                self.assertEqual(amount_after+float(params['amount']), self.amount_start)
            except AssertionError as e:
                raise e

            # 查询invest表
            invest_sql = "SELECT * FROM invest WHERE MemberID='{}' ORDER BY CreateTime DESC LIMIT 1".format(conf.get_conf_str("regex", 'memberid'))
            invest_result = mysql.fecth_one(sql=invest_sql)
            if invest_result:
                list_1 = []
                list_1.append(invest_result['MemberID'])
                list_1.append(invest_result['LoanId'])
                list_1.append(float(invest_result['Amount']))
                list_2 = []
                list_2.append(eval(params['memberId']))
                list_2.append(eval(getattr(Context, 'loan_id')))
                list_2.append(eval(params['amount']))
                try:
                    self.assertListEqual(list_1, list_2)
                except AssertionError as e:
                    raise e
            else:
                print("invest表中未生成数据")

            # 查询financeLog表
            financeLog_sql = "SELECT * FROM financelog WHERE PayMemberId='{}' ORDER BY CreateTime DESC LIMIT 1".format(conf.get_conf_str("regex", 'memberid'))
            financeLog_result = mysql.fecth_one(sql=financeLog_sql)
            if invest_result:
                list_1 = []
                list_1.append(financeLog_result['PayMemberId'])
                list_1.append(financeLog_result['IncomeMemberId'])
                list_1.append(float(financeLog_result['Amount']))
                list_2 = []
                list_2.append(eval(params['memberId']))
                list_2.append(eval(conf.get_conf_str("regex", 'borrower_memberid')))
                list_2.append(eval(params['amount']))
                try:
                    self.assertListEqual(list_1, list_2)
                except AssertionError as e:
                    raise e
            else:
                print("financeLog表中未生成数据")



