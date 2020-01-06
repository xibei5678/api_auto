#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : do_http.py
@Date  : 2020/1/6 0006 15:05
@Author: xibei
'''

import requests
import json


class DoHttp:

    def __init__(self):
        self.session = requests.session()

    def __call__(self, method, url, data, is_json=False, **kwargs):

        method = method.lower()
        if isinstance(data, dict) or isinstance(data, str):
            if isinstance(data, dict):
                data = data
            elif isinstance(data, str):
                try:
                    data = json.loads(data)
                except Exception as e:
                    print(e)
                    data = eval(data)
        else:
            print("{}格式不正确".format(data))

        if method == 'get':
            res = self.session.request(url=url, data=data)
        if method == 'post':
            if isinstance(is_json, bool):
                if is_json:
                    res = self.session.post(url=url, json=data)
                else:
                    res = self.session.post(url=url, data=data)
            else:
                print("is_json不是bool值")

