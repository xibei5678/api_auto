#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : constant.py
@Date  : 2020/3/23 0023 16:52
@Author: xibei
'''


import os
base_dir = os.path.dirname(os.path.dirname(__file__))
# print(base_dir)

common_dir = os.path.join(base_dir, 'common')

conf_dir = os.path.join(base_dir, 'conf')  # 配置文件地址
global_conf = os.path.join(conf_dir, 'global.conf')  # 全局配置文件路径
online_conf = os.path.join(conf_dir, 'online.conf')  # 线上环境配置文件路径
test_conf = os.path.join(conf_dir, 'test.conf')  # 测试环境配置文件路径

test_cases_dir = os.path.join(base_dir, 'test_cases')

test_data_dir = os.path.join(base_dir, 'test_data')

test_report_dir = os.path.join(base_dir, 'test_report')