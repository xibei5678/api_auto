# -*- coding: utf-8 -*-
# @Time : 2019/12/19 21:32
# @Author : xibei
# @filename : python_20191219_requests模块.py
# @description ：

'''requests 模块'''

# 1.作用：用于发起http协议的请求
# 2. requests 模块是第三方库，需安装：pip install requests
# 3.使用时需要引用：import requests
# 4.用法：requests.get()、requests.post()、requests.delete()等
# 5.返回结果为信息实体（object）,查看响应报文有object.text或object.json（）
#   text：可查看所有形式的响应报文
#   json（): 查看响应信息为字典或json形式的报文

import requests

url = 'https://www.baidu.com/'

# get 请求
res_get = requests.get(url)

# post请求
res_post = requests.post(url)

'''# 响应结果中包含：状态码(object.status_code)、响应头（object.headers）、响应报文(object.text)'''

# 查看响应报文
# print(res_get.text)
# print(res_post.text)

# 查看响应头
# print(res_get.headers)

# 查看响应状态
# print(res_get.status_code)


'''请求信息：请求头(object.request.headers)、请求正文、请求地址、请求方式'''

# 查看请求头
# print(res_get.request.headers)

# 查看请求地址
# print(res_get.url)


'''需要cookies的请求示例'''

# 方式一

# 登录 地址和数据
login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
login_data = {'mobilephone': 18688773467, 'pwd': '123456'}

login_res = requests.get(url=login, params=login_data)
print(login_res.json())  # 查看响应正文
print(login_res.cookies)  # 查看cookies，cookies是类字典
print(login_res.cookies['JSESSIONID'])  # 获取cookies值

# 充值 地址和数据
recharge = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
recharge_data = {'mobilephone': 18688773467, 'amount': '1000'}

# 充值失败
# recharge_res = requests.post(url=recharge, data=recharge_data)  # 充值需登录，发起请求时未带cookies，因http请求时无状态
# print(recharge_res.json())  # 充值失败：{'data': None, 'status': 0, 'msg': '抱歉，请先登录。', 'code': None}
# 充值成功
recharge_res = requests.post(url=recharge, data=recharge_data, cookies=login_res.cookies)
print(recharge_res.json())

# 方式二

# 建立会话
res = requests.session()
#登录请求
res_login = res.get(url=login, params=login_data)
print('登录请求的响应报文：', res_login.json())
#充值请求
res_recharge = res.post(url=recharge, data=recharge_data)
print('充值请求的响应报文：', res_recharge.json())
