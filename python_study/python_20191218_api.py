#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191218_api.py
@Date  : 2019/12/18 0018 16:33
@Author: xibei
'''

''' 接口 '''

# 1. 定义：模块与模块之间的衔接桥梁

# 2. 分类：
#   1） 广义分类：内部接口、外部接口
#   2） 按不同的协议：http、webservice、 dubbo 、socket
#       http协议下的请求方式分为：get post delete head option
#       webservice协议接口 实质是经过封装的http post请求

# 3. http 协议请求
#   1.请求数据：
#          1）请求头示例如下：#并不是所有请求都需要
#                   User-Agent：产生请求的浏览器类型。
#                   Accept：客户端可识别的内容类型列表。
#                   Host：请求的主机名，允许多个域名同处一个IP地址，即虚拟主机
#                   Accept_Encoding:
#                   Accept_Language:
#                   Connection:
#                   Cookie:
#                   If-None-Match:
#                   详细参考：https://jingyan.baidu.com/article/375c8e19770f0e25f2a22900.html?pu=&st=1&bd_page_type=1&os=&rst=
#          2）请求正文（请求参数）

#   2. 响应数据：
#           1）状态码：200（正常）、302（重定向）、304（未修改）、403（禁止）、404（找不到）、500（内部服务器错误）、504（超时）
#           2）响应头
#           3）响应报文