#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : run_http_request.py
@Date  : 2019/12/24 0024 10:58
@Author: xibei
'''

import unittest
from python_api_test_first.unittest_http import HttpUnittest
import HTMLTestRunnerNew
from python_api_test_first.do_excel import DoExcel

test_data_1 = [{'title': '登录_成功', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'method': 'get',
              'params': {'mobilephone': 18688773467, 'pwd': '123456'}, 'expect': '登录成功'},
             {'title': '登录_手机号错误', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'method': 'get',
              'params': {'mobilephone': 18688773467, 'pwd': '123'}, 'expect': '用户名或密码错误'},
             {'title': '登录_密码错误', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'method': 'get',
              'params': {'mobilephone': 186887767, 'pwd': '123456'}, 'expect': '用户名或密码错误'},
             {'title': '充值_成功', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge', 'method': 'post',
              'params': {'mobilephone': 18688773467, 'amount': '1000'}, 'expect': '充值成功'},
             {'title': '充值_手机号错误', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge', 'method': 'post',
              'params': {'mobilephone': 1868871767, 'amount': '1000'}, 'expect': '手机号码格式不正确'},
             {'title': '充值_金额格式错误', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge', 'method': 'post',
              'params': {'mobilephone': 18688773467, 'amount': '1000.001'}, 'expect': '输入金额的金额小数不能超过两位'}]

test_data_2 = DoExcel().do_excel('test_case.xlsx', 'Sheet1')

for i in range(6):
    print(test_data_1[i]['url'])
    print(type(test_data_1[i]['url']))
    print(test_data_2[i]['url'])
    print(type(test_data_2[i]['url']))
    print()

    print(test_data_1[i]['params'])
    print(type(test_data_1[i]['params']))
    print(test_data_2[i]['params'])
    print(type(test_data_2[i]['params']))
    print()


# for item in test_data_2:
#     # print(item['title'])
#     # print(type(item['title']))
#     # print(item['url'])
#     # print(type(item['url']))
#     # print(item['method'])
#     # print(type(item['method']))
#     # print(item['params'])
#     # print(type(item['params']))
#     # print(item['expect'])
#     # print(type(item['expect']))
#     # print()





# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# for item in test_data:
#     suite.addTest(HttpUnittest(title=item['title'], url=item['url'], method=item['method'], params=item['params'], expect=item['expect'], methodName='test_http'))
#
#
# with open('unittest_result.html', 'wb+') as file:
#     HTMLTestRunnerNew.HTMLTestRunner(file, title='单元测试结果', description='登录和充值测试用例').run(suite)
