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

my_logger.debug('这是一个debug日志错误')
my_logger.info('这是一个info日志错误')
my_logger.warning('这是一个warning日志错误')
my_logger.error('这是一个error日志错误')
my_logger.critical('这是一个critical日志错误')




