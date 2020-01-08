#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : do_http.py
@Date  : 2020/1/6 0006 15:05
@Author: xibei
'''

import requests
import json
from python_api_test_two.do_logger import DoLog
my_log = DoLog()


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
            my_log.error("{}格式不正确".format(data))

        if method == 'get':
            res = self.session.request(method='get', url=url, params=data, **kwargs)  # get方式字典数据类型需要用params接收
        elif method == 'post':
            if isinstance(is_json, bool):
                if is_json:
                    res = self.session.request(method='post', url=url, json=data, **kwargs)
                else:
                    res = self.session.request(method='post', url=url, data=data, **kwargs)
            else:
                my_log.error("is_json不是bool值")
        elif method == "put":
            res = self.session.request(method="put", url=url, data=data, **kwargs)
        elif method == "delete":
            res = self.session.request(method="delete", url=url, **kwargs)
        else:
            res = None
            my_log.error("{}请求方式错误".format(method))

        return res

    def close_request(self):
        return self.session.close()

if __name__ == '__main__':

    # test_data = [{'title': '登录_成功', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'method': 'get',
    #               'params': {'mobilephone': 18688773467, 'pwd': '123456'}, 'expect': '登录成功'},
    #              {'title': '登录_手机号错误', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'method': 'get',
    #               'params': {'mobilephone': 18688773467, 'pwd': '123'}, 'expect': '用户名或密码错误'},
    #              {'title': '登录_密码错误', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'method': 'get',
    #               'params': {'mobilephone': 186887767, 'pwd': '123456'}, 'expect': '用户名或密码错误'},
    #              {'title': '充值_成功', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge', 'method': 'post',
    #               'params': {'mobilephone': 18688773467, 'amount': '1000'}, 'expect': '充值成功'},
    #              {'title': '充值_手机号错误', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge', 'method': 'post',
    #               'params': {'mobilephone': 1868871767, 'amount': '1000'}, 'expect': '手机号码格式不正确'},
    #              {'title': '充值_金额格式错误', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge', 'method': 'post',
    #               'params': {'mobilephone': 18688773467, 'amount': '1000.001'}, 'expect': '输入金额的金额小数不能超过两位'}]

    # req = DoHttp()
    # for item in test_data:
    #     res = req(url=item['url'], method=item['method'], data=item['params'])
    #     print(res.json())
    #     req.close_request()

# 车辆新增

    req = DoHttp()
    url = 'http://49.4.52.176/api/vehicleTerminal/save'
    method = 'post'
    params = {"vehicleVin":"","vehicleModel":"222","vehicleSm":"333","detectionOrg":"444","dischargeStandard":"555","responsibleName":"666","responsiblePhone":"13230151561","responsibleEmail":"266555@qq.com"}
    res = req(method, url, params, is_json=True)
    print(res.json())