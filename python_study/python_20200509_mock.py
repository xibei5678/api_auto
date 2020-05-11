#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20200509_mock.py
@Date  : 2020/5/9 0009 15:06
@Author: xibei
'''

import requests

class Payment:# 支付类

    def request_third_api(self, card_num, amount):
        '''
        请求第三方支付接口，并返回状态码
        :param card_num: 卡号
        :param amount: 支付金额
        :return: 返回状态码，200代表成功，500代表支付异常失败
        '''
        req_url = "http://third.payment.com"
        data = {"card_num": card_num, "amount": amount}
        res = requests.post(req_url, data)
        return res.status_code

    def do_pay(self, user_id, card_num, amount):

        '''
        支付
        :param user_id: 用户id
        :param card_num: 卡号
        :param amount: 支付金额
        :return:
        '''

        try:
            resp = self.request_third_api(card_num, amount)
        except TimeoutError:
            resp = self.request_third_api(card_num, amount)

        if resp == 200:
            print('{0}支付{1}成功'.format(user_id, amount))
            return 'success'

        if resp == 500:
            print('{0}支付{1}失败'.format(user_id, amount))
            return 'fail'


''' mock '''
# 1. mock是python支持的测试库，使用mock对象替代指定python对象，已达到模拟对象的行为目的
# 2.安装：已集成到unittest中
# 3.用法：
# 定义mock类
# class Mock（spec=None,side_effect=None,return_value=DEFAULT,name=None）
#       secp:定义mock对象的属性值，可以是一个列表，字符串，甚至一个对象或者实例
#       side_effect： 可以用来抛出异常或者动态改变返回值，它必须是一个iteator，它会覆盖return value
#       return_value：定义mock方法的返回值，它可以是一个值，可以是一个对象
#       name：作为mock对象的一个标示，在print时可以看到



'''mock 练习'''

import unittest
from unittest import mock

class TestPayment(unittest.TestCase):

    def setUp(self):
        self.payment = Payment()

    def test_success(self):
        # 模拟payment.request_third_api 的返回值为200
        self.payment.request_third_api = mock.Mock(return_value=200)
        resp = self.payment.do_pay(user_id=1, card_num='45678', amount=100)
        self.assertEqual('success', resp, '测试支付成功')

    def test_fail(self):
        # 模拟payment.request_third_api 的返回值为500
        self.payment.request_third_api = mock.Mock(return_value=500)
        resp = self.payment.do_pay(user_id=1, card_num='45678', amount=100)
        self.assertEqual('fail', resp, '测试支付失败')

    def test_timeout_success(self):
        # 模拟payment.request_third_api 的返回值为先超时，再成功
        self.payment.request_third_api = mock.Mock(side_effect=[TimeoutError, 200])
        resp = self.payment.do_pay(user_id=1, card_num='45678', amount=100)
        self.assertEqual('success', resp, '测试支付成功')

    def test_timeout_fail(self):
        # 模拟payment.request_third_api 的返回值为先超时，再失败
        self.payment.request_third_api = mock.Mock(side_effect=[TimeoutError, 500])
        resp = self.payment.do_pay(user_id=1, card_num='45678', amount=100)
        self.assertEqual('fail', resp, '测试支付失败')


