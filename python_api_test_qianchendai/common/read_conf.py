#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : read_conf.py
@Date  : 2020/3/23 0023 16:50
@Author: xibei
'''

import configparser
from python_api_test_qianchendai.common.constant import *

class ReadConf:

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(global_conf, encoding='utf-8')
        value = self.conf.get("button", "switch")
        if value == "on":
            self.conf.read(test_conf, encoding="utf-8")

        elif value == "off":
            self.conf.read(online_conf, encoding="utf-8")

    def get_conf_str(self, section, option):  # 从配置文件中获取的值为str
        return self.conf.get(section, option)

    def get_conf_int(self, section, option):   # 从配置文件中获取的值为int
        return self.conf.getint(section, option)

    def get_conf_boolean(self, section, option):   # 从配置文件中获取的值为boolean
        return self.conf.getboolean(section, option)

    def get_conf_float(self, section, option):   # 从配置文件中获取的值为float
        return self.conf.getfloat(section, option)



if __name__ == '__main__':
    read_conf = ReadConf()
    url =read_conf.get_conf_str(section="api", option="url")
    print(url)


