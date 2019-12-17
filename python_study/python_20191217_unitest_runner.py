#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191217_unitest_runner.py
@Date  : 2019/12/17 0017 17:26
@Author: xibei
'''

import unittest
from python_study.python_20191217_unittest import TestSai

# 创建测试集
suite = unittest.TestSuite()

# 加载用例

# 1）.addTest 一个用例一个用例的添加
suite.addTest(TestSai('test_add_positive'))
suite.addTest(TestSai('test_add_negative'))
suite.addTest(TestSai('test_add_zero'))

# 2) TestLoader 测试类、模块添加
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSai))  # 直接加载测试类,导入的时候只具体到类名
# suite.addTest(unittest.TestLoader().loadTestsFromModule('python_20191217_unittest'))  # 直接加载测试类的模块名，导入的时候只具体到模块名


# 执行用例
runner = unittest.TextTestRunner().run(suite)