#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : read_conf.py
@Date  : 2019/12/30 0030 17:52
@Author: xibei
'''


import configparser

class ReadConf:

    def read_conf(self, file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding='utf-8')
        value = cf.get(section, option)
        return value