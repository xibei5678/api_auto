#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : unittest_http.py
@Date  : 2019/12/23 0023 17:42
@Author: xibei
'''


import unittest

from python_api_test_first.http_requests import HttpRequests

COOKIES = None


class HttpUnittest(unittest.TestCase):

    def __init__(self, title, url, method, params, expect, methodName):
        '''

        :param url:请求地址
        :param method: 请求方法
        :param params: 参数
        :param expect: 期望值
        :param methodName: 用例方法名
        '''
        super(HttpUnittest, self).__init__(methodName)  # 超继承
        self.title = title
        self.url = url
        self.method = method
        self.params = params
        self.expect = expect


    def setUp(self):
        print("********开始进入测试********")

    def tearDown(self):
        print("********用例测试结束********")

    def test_http(self):
        print("正在执行用例：{}".format(self.title))
        print("请求地址:{}".format(self.url))
        print("请求方法:{}".format(self.method))
        print("请求参数:{}".format(self.params))
        print("期望结果:{}".format(self.expect))
        global COOKIES
        res = HttpRequests(method=self.method, url=self.url, params=self.params, cookies=COOKIES)
        if res.response_cookies():  # 当cookies有值时 就修改COOKIES
            # global COOKIES # 在此处声明 会报错，需在使用COOKIES之前声明
            COOKIES = res.response_cookies()
        if res.response_json():  # 是否支持json形式
            print("返回结果为：{}".format(res.response_json()))
            try:
                self.assertEqual(self.expect, res.response_json()['msg'])
            except Exception as e:
                print("报错了：{}".format(e))
                raise e
        else:
            print(res.response_status_code())
            print(res.response_text())



