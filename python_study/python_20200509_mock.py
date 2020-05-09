#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20200509_mock.py
@Date  : 2020/5/9 0009 15:06
@Author: xibei
'''

''' mock '''
# 1. mock是python支持的测试库，使用mock对象替代指定python对象，已达到模拟对象的行为目的
# 2.安装：已集成到unittest中
# 3.用法：
# 定义mock类
# class Mock（spec=None,side effect=None,return value=DEFAULT,name=None）
#       secp:定义mock对象的属性值，可以是一个列表，字符串，甚至一个对象或者实例
#       side effect： 可以用来抛出异常或者动态改变返回值，它必须是一个iteator，它会覆盖return value
#       return value：定义mock方法的返回值，它可以是一个值，可以是一个对象
#       name：作为mock对象的一个标示，在print时可以看到