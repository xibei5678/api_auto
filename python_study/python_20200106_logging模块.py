#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20200106_logging模块.py
@Date  : 2020/1/6 0006 11:04
@Author: xibei
'''


''' logging 日志'''

# 1. python自带模块
# 2. 用于日志收集
# 3. root logger 系统自带默认日志收集器
#    1).错误等级分为：debug、info、warning、error、critical 五个等级，依次越来越严重
#    2）. 默认收集并输出warning级别以上的日志
#    3）. 默认输出到控制台（console）
# 4. 注意：
#    如:DoLog类
#   1）：直接在init函数中编写构造logger，在引用时容易出现输出到console的信息不能输出到测试报告中
#   2）：在添加输出渠道后，未移除输出渠道，在被其他模块引用后会出现日志信息重复
#


import logging
import time

# 使用系统自带的日志收集器 控制台输出warning和warning以上的日志

# logging.debug('这是一个debug日志错误')
# logging.info('这是一个info日志错误')
# logging.warning('这是一个warning日志错误')
# logging.error('这是一个error日志错误')
# logging.critical('这是一个critical日志错误')


# 设置自己的日志收集器

# 第一步: 创建一个自己日志收集器
my_logger = logging.getLogger("my_logger")
# 第二步：设置日志收集级别
my_logger.setLevel('DEBUG')
# 第三步：设置日志信息输出格式
log_format = logging.Formatter('[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]')
# 第四步：设置日志输出渠道 handle
# 1）控制台
ch = logging.StreamHandler()  # 输出到控制台
ch.setLevel('WARNING')  # 设置输出级别
ch.setFormatter(log_format)  # 设置输出日志信息格式

# 2）输出到txt文档中
fh = logging.FileHandler('{}_log.txt'.format(time.strftime('%Y-%m-%d', time.localtime(time.time()))), encoding='utf-8') # 输出到txt文档中
fh.setLevel('DEBUG')  # 设置输出级别
fh.setFormatter(log_format)  # 设置输出日志信息格式


# 第五步:对接
my_logger.addHandler(ch)  #把输出渠道添加给logger收集器
my_logger.addHandler(fh)

# my_logger.debug('这是一个debug日志错误')
# my_logger.info('这是一个info日志错误')
# my_logger.warning('这是一个warning日志错误')
# my_logger.error('这是一个error日志错误')
# my_logger.critical('这是一个critical日志错误')



# 示例（对应注意中的第一点）

class DoLog:

    def __init__(self):
        self.my_log = logging.getLogger('my_log')
        simple_formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - [日志信息]:%(message)s')
        # 日志收集等级
        self.my_log.setLevel('DEBUG')

        # 日志输出渠道--控制台
        self.ch = logging.StreamHandler()
        self.ch.setLevel('INFO')
        self.ch.setFormatter(simple_formatter)

        # 日志输出渠道--txt文档
        self.fh = logging.FileHandler('log.txt', encoding='utf-8')
        self.fh.setLevel('ERROR')
        self.fh.setFormatter(simple_formatter)

        # 对接
        self.my_log.addHandler(self.ch)
        self.my_log.addHandler(self.fh)

    def debug(self, msg):
        return self.my_log.debug(msg)

    def info(self, msg):
        return self.my_log.info(msg)

    def warning(self, msg):
        return self.my_log.warning(msg)

    def error(self, msg):
        return self.my_log.error(msg)

    def critical(self, msg):
        return self.my_log.critical(msg)

if __name__ == '__main__':

    my_logger = DoLog()
    my_logger.debug('这是一个debug日志错误')
    my_logger.info('这是一个info日志错误')
    my_logger.warning('这是一个warning日志错误')
    my_logger.error('这是一个error日志错误')
    my_logger.critical('这是一个critical日志错误')