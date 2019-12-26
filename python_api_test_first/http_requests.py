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

    def response_status_code(self):
        return  self.res.status_code

    # def response_code(self):
    #     return self.response_json()['code']
    #
    # def response_msg(self):
    #     return self.response_json()['msg']



if __name__ == '__main__':
    from python_api_test_first.do_excel import DoExcel

    COOKIES = None
    test_data = DoExcel().do_excel('test_case.xlsx', 'Sheet1')
    # global()
    for item in test_data:
        title = item['title']
        url = item['url']
        method = item['method']
        params = eval(item['params'])
        expect = item['expect']
        print("********开始进入测试********")
        print("正在执行用例：{}".format(title))
        print("请求地址:{}".format(url))
        print("请求方法:{}".format(method))
        print("请求参数:{}".format(params))
        print("期望结果:{}".format(expect))
        res = HttpRequests(url, method, params, cookies=COOKIES)
        print(res.response_json())
        if res.response_cookies():  # 当cookies有值时 就修改COOKIES
            # global COOKIES # 在此处声明 会报错，需在使用COOKIES之前声明
            COOKIES = res.response_cookies()

        print("********用例执行完成********")
        print()




