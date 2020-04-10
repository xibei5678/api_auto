#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : http_requets.py
@Date  : 2020/1/17 0017 16:50
@Author: xibei
'''


import requests
import json

class HttpRequest:

    def __init__(self, method, url, params=None, cookies=None, headers=None, is_json=False):
        try:
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
        except Exception as e:
            raise e

    def get_status_code(self):  # 获取返回状态码
        return self.res.status_code

    def get_text(self):  # 获取返回体
        res = self.res.text
        return res
        # return json.loads(res)  # 将返回的字符串序列化为python字典格式

    def get_json(self):  # 获取返回的字典对象
        return self.res.json()


if __name__ == '__main__':

    url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
    params = {"mobilephone": "19100000001", "pwd": "123456"}
    method = 'post'
    a = HttpRequest(method, url, params)
    print(a.get_text())





