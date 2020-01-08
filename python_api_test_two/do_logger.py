#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : do_logger.py
@Date  : 2020/1/6 0006 15:06
@Author: xibei
'''

import os
import logging
from python_api_test_two.do_conf import DoConf
import time
from python_api_test_two.basic import base_path, conf_path

conf_value = DoConf(conf_path)  # 创建实例


#
class DoLog:

    def do_log(self, level, msg):
        my_log = logging.getLogger(conf_value('log', 'log_name'))
        simple_formatter = logging.Formatter(conf_value('log', 'simple_formatter'))  # 从配置文件中获取格式
        particular_formatter = logging.Formatter(conf_value('log', 'particular_formatter'))
        # 日志收集等级
        my_log.setLevel('DEBUG')

        # 日志输出渠道--控制台
        ch = logging.StreamHandler()
        ch.setLevel(conf_value('log', 'console_level'))
        ch.setFormatter(simple_formatter)

        # 日志输出渠道--txt文档
        fh = logging.FileHandler(os.path.join(base_path, '{}_log.txt'.format(time.strftime('%Y-%m-%d', time.localtime(time.time())))), encoding='utf-8')
        fh.setLevel(conf_value('log', 'file_level'))
        fh.setFormatter(particular_formatter)

        # 对接
        my_log.addHandler(ch)
        my_log.addHandler(fh)

        if level == 'DEBUG':
            result = my_log.debug(msg)
        elif level == 'INFO':
            result = my_log.info(msg)
        elif level == 'WARNING':
            result = my_log.warning(msg)
        elif level == 'ERROR':
            result = my_log.error(msg)
        elif level == 'CRITICAL':
            result = my_log.critical(msg)
        else:
            result = None

        # 移除输出渠道 handle
        my_log.removeHandler(ch)
        my_log.removeHandler(fh)

        return result

    def debug(self, msg):
        return self.do_log('DEBUG',msg)

    def info(self, msg):
        return self.do_log('INFO', msg)

    def warning(self, msg):
        return self.do_log('WARNING', msg)

    def error(self, msg):
        return self.do_log('ERROR', msg)

    def critical(self, msg):
        return self.do_log('CRITICAL', msg)



if __name__ == '__main__':

    my_logger = DoLog()
    my_logger.debug('这是一个debug日志错误')
    my_logger.info('这是一个info日志错误')
    my_logger.warning('这是一个warning日志错误')
    my_logger.error('这是一个error日志错误')
    my_logger.critical('这是一个critical日志错误')

    # print(base_path)
    # print(os.path.join(base_path, '{}_log.txt'.format(time.strftime('%Y-%m-%d', time.localtime(time.time())))))


