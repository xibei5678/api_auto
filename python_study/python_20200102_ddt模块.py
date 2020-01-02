#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20200102_ddt模块.py
@Date  : 2020/1/2 0002 10:24
@Author: xibei
'''



''' ddt 模块'''

# 1. ddt： data drive test 数据驱动测试
# 2. @ddt 装饰器：用于单元测试中装饰测试类，@data装饰测试方法，ddt和data搭配使用才生效
# 3. 用法：
# @ddt
# class 类名
# @data（动态参数）
# @unpack # 对参数再拆分，并需要等量的变量去接收否则报错
# def test_函数名（self,参数）： # 被装饰的测试用例函数可以传参数
# 4. 第三方库 需安装：pip install ddt
# 5. ddt装饰后的测试用例不能被识别，加载用例需使用loader进行加载


''' * 符号 '''
# 1.有去外套的作用
# 2. 只能去一层外套
a = (1, 2, 3, 4, 5, 6)
a_1 = [[1, 2, 3], [4, 5, 6]]

def test_1(*args):
    print(args)

# test_1(a)  # 结果为：((1, 2, 3, 4, 5, 6),)  # a是以元组整个传入,只有一个参数：test_1((1, 2, 3, 4, 5, 6))
# test_1(*a)  # 结果为：(1, 2, 3, 4, 5, 6)    # *a 是将a去外套后，传入6个参数为：test_1(1, 2, 3, 4, 5, 6)
# test_1(a_1)  # 结果为：([[1, 2, 3], [4, 5, 6]],)
# test_1(*a_1)  # 结果为：([1, 2, 3], [4, 5, 6]) # *a_1 是将a_1去外套后，传入2个参数为：test_1([1, 2, 3],[4, 5, 6])
# test_1(**a_1) # 报错


import unittest
from ddt import ddt,data,unpack

test_data = [{'title': '登录_成功', 'url': 'http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'method': 'get',
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



@ddt
class HttpReq(unittest.TestCase):
# 方式一：
#     @data(*test_data)
#     def test_res(self, item):  # item变量接收去外套后的test_data
#         print("正在执行用例：{}".format(item['title']))
#         print("请求地址:{}".format(item['url']))
#         print("请求方法:{}".format(item['method']))
#         print("请求参数:{}".format(item['params']))
#         print("期望结果:{}".format(item['expect']))
#         print('='*50)
#         print()

# 方式二：
    @data(*test_data)
    @unpack  # unpack对test_data去外套后的参数（item）再拆分，item为字典时，下方传入的参数变量名需与key对应，其他数据类型除外
    def test_res(self, title, url, method, params, expect):
        print("正在执行用例：{}".format(title))
        print("请求地址:{}".format(url))
        print("请求方法:{}".format(method))
        print("请求参数:{}".format(params))
        print("期望结果:{}".format(expect))
        print('='*50)
        print()


if __name__ == '__main__':
    import unittest
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(HttpReq))
    unittest.TextTestRunner().run(suite)
