#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : read_conf.py
@Date  : 2020/3/23 0023 16:50
@Author: xibei
'''

import configparser
from python_api_test_qianchendai.common.constant import *

class DoConf:

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(global_conf, encoding='utf-8')
        value = self.conf.get("button", "switch")
        if value == "on":
            self.file_name = test_conf
        elif value == "off":
            self.file_name = online_conf
        self.conf.read(self.file_name, encoding="utf-8")

    def get_conf_str(self, section, option):  # 从配置文件中获取的值为str
        return self.conf.get(section, option)

    def get_conf_int(self, section, option):   # 从配置文件中获取的值为int
        return self.conf.getint(section, option)

    def get_conf_boolean(self, section, option):   # 从配置文件中获取的值为boolean
        return self.conf.getboolean(section, option)

    def get_conf_float(self, section, option):   # 从配置文件中获取的值为float
        return self.conf.getfloat(section, option)

    def write_conf(self, section, option, value):  # 向配置文件中写入

        if section not in self.conf.sections():
            self.conf.add_section(section)
            self.conf.set(section=section, option=option, value=value)
            with open(self.file_name, "w+", encoding="utf-8") as f:
                self.conf.write(f)
        else:
            self.conf.set(section=section, option=option, value=value)
            with open(self.file_name, "w+", encoding="utf-8") as f:
                self.conf.write(f)


if __name__ == '__main__':
    read_conf = DoConf()
    # url =read_conf.get_conf_str(section="api", option="url")
    # print(url)
    # read_conf.write_conf(r'F:\python_lemon\api_test\python_study\python_20191230_配置文件.conf', "配置", "名字", "多多")

