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

    def __init__(self, url, method, params, expect, methodName):
        super(HttpUnittest, self).__init__(methodName)  # 超继承
        self.url = url
        self.method = method
        self.params = params
        self.expect = expect


    def test_http(self):

        res = HttpRequests(method=self.method, url=self.url, params=self.params, cookies=COOKIES)
        global
        if res.response_cookies():

            COOKIES = res.response_cookies()



