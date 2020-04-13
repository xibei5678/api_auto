#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : test_register_new.py
@Date  : 2020/4/10 0010 15:26
@Author: xibei
'''

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
# sql = 'SELECT * FROM member WHERE MobilePhone !="" ORDER BY MobilePhone DESC LIMIT 1'





@ddt
class TestRegister(TestCase):


    def setUp(self):
        self.mysql = DoMysql()
        print("*" * 20 + "用例执行准备" + "*" * 20)

    @data(*cases_data)
    def test_register(self, case):
        if re.search(string=case.params, pattern="\$\{(.*?)\}"):
            # 从配置文件中获取normal_name (替换值)
            repl = conf.get_conf_str('regex', 'normal_name')
            conf.write_conf('regex', 'normal_name', str(int(repl)+1))
            params = re.sub(pattern='\$\{(.*?)\}', repl=repl, string=case.params)  # repl值需为str
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
            do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)
        except AssertionError as e:
            result = 'fail'
            do_excel.write_by_case_id(sheet_name=sheet_name, case_id=case.id, column=9, value=result)
            raise e

        add_sql = 'SELECT * FROM member WHERE MobilePhone ={}'.format(params['mobilephone'])
        add_user_msg = self.mysql.fecth_one(add_sql)

        if res.get_json()['msg'] == '注册成功':
            if add_user_msg:
                print(add_user_msg)
                print(add_user_msg['MobilePhone'])
                print(add_user_msg['LeaveAmount'])
                self.assertEqual(add_user_msg['MobilePhone'], repl)
                self.assertEqual(float(add_user_msg['LeaveAmount']), 0.00)
            else:
                print("数据库新增用户信息失败")
        # else:
        #     self.assertEqual(add_user_msg, None)
        self.mysql.close_cursor()

    def tearDown(self):

        self.mysql.close_connect()
        print("*"*20+"用例执行完成"+"*"*20)




