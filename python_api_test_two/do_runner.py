#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : do_runner.py
@Date  : 2020/1/6 0006 15:08
@Author: xibei
'''

import unittest
from python_api_test_two.do_unittest_case import DoUnittest
import HTMLTestRunnerNew
import time
from python_api_test_two.basic import *


# 测试报告名字
file_name = os.path.join(base_path, '{}_report.html'.format(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
# 创建测试集
suite = unittest.TestSuite()
# 加载用例
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(DoUnittest))
# 输出html测试报告
with open(file_name, "wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file, title='单元测试报告', description='登录、充值接口测试', tester='溪贝')
    runner.run(suite)