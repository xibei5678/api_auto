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


'''cookie session'''
# 1.Cookie实际上是一小段的文本信息。客户端请求服务器，如果服务器需要记录该用户状态，就使用response向客户端浏览器颁发一个Cookie。
#       客户端浏览器会把Cookie保存起来。当浏览器再请求该网站时，浏览器把请求的网址连同该Cookie一同提交给服务器。
#       服务器检查该Cookie，以此来辨认用户状态。服务器还可以根据需要修改Cookie的内容。
#
# 2.Session是另一种记录客户状态的机制，不同的是Cookie保存在客户端浏览器中，而Session保存在服务器上。
#   客户端浏览器访问服务器的时候，服务器把客户端信息以某种形式记录在服务器上。这就是Session。
#   客户端浏览器再次访问时只需要从该Session中查找该客户的状态就可以了。

# 3. Cookie通过在客户端记录信息确定用户身份，Session通过在服务器端记录信息确定用户身份

# 4. 如果说Cookie机制是通过检查客户身上的“通行证”来确定客户身份的话，那么Session机制就是通过检查服务器上的“客户明细表”来确认客户身份。
#    Session相当于程序在服务器上建立的一份客户档案，客户来访的时候只需要查询客户档案表就可以了。

