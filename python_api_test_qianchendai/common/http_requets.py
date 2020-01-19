#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : http_requets.py
@Date  : 2020/1/17 0017 16:50
@Author: xibei
'''


import requests

class HttpRequest:

    def __init__(self, method, url, params=None, cookies=None, headers=None, is_json=False):
        if method == 'get':
            self.res = requests.get(url=url, params=params, cookies=cookies, headers=headers)
        elif method == 'post':
            if isinstance(is_json, bool):
                if is_json:
                    self.res = requests.post(url=url, json=params, cookies=cookies, headers=headers)
                else:
                    self.res = requests.post(url=url, data=params, cookies=cookies, headers=headers)
            else:
                print('is_json的值为{}，输入类型错误，请检查'.format(is_json))
        elif method == 'put':
            self.res = requests.put(url=url, data=params, cookies=cookies, headers=headers)
        elif method == 'delete':
            self.res = requests.delete(url=url, data=params, cookies=cookies, headers=headers)
        elif method == 'patch':
            self.res = requests.patch(url=url, data=params, cookies=cookies, headers=headers)

    def get_status_code(self):
        return self.res.status_code

    def get_text(self):
        return self.res.text

    def get_json(self):
        return self.res.json()


