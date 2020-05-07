#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : run_test_cases.py
@Date  : 2020/5/6 0006 14:52
@Author: xibei
'''


import unittest
import HTMLTestRunnerNew
from python_api_test_qianchendai.common.constant import *


file_name = os.path.join(test_report_dir,'repots','auto_api_report.html')

discover = unittest.defaultTestLoader.discover(test_cases_dir, 'test_*')

with open(file_name, "wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title='auto_api_test_report', description='接口自动化测试用例', tester='溪贝')
    runner.run(discover)



