#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : http_requests.py
@Date  : 2019/12/20 0020 16:23
@Author: xibei
'''


import requests

class HttpRequests:

    def __init__(self, url, method, params=None, cookies=None, headers=None):

        '''

        :param url: url地址
        :param method: 请求方式
        :param params: 请求参数
        :param cookies: cookies
        :param headers: 请求头

        '''

        try:

            if method == 'get':
                self.res = requests.get(url=url, params=params, cookies=cookies, headers=headers)

            if method == 'post':
                self.res = requests.post(url=url, params=params, cookies=cookies, headers=headers)

            if method == 'delete':
                self.res = requests.delete(url=url, params=params, cookies=cookies, headers=headers)

            if method == 'patch':
                self.res = requests.patch(url=url, params=params, cookies=cookies, headers=headers)

            if method =='options':
                self.res = requests.options(url=url, params=params, cookies=cookies, headers=headers)

            if method == 'head':
                self.res = requests.head(url=url, params=params, cookies=cookies, headers=headers)

            if method == 'put':
                self.res = requests.put(url=url, params=params, cookies=cookies, headers=headers)

        except Exception as e:
            raise e


    def response_text(self):
        return self.res.text

    def response_json(self):
        return self.res.json()

    def response_cookies(self):
        return self.res.cookies

    # def response_code(self):
    #     return self.response_json()['code']
    #
    # def response_msg(self):
    #     return self.response_json()['msg']


if __name__ == '__main__':

    # 登录地址和数据
    login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    login_data = {'mobilephone': 18688773467, 'pwd': '123456'}
    res = HttpRequests(login, 'get', login_data)
    print(res.response_json())

    # #充值 地址和数据
    # recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
    # recharge_data = {'mobilephone': 18688773467, 'amount': '1000'}

