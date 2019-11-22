#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : pythoh_20191121_循环语句练习.py
@Date  : 2019/11/21 0021 16:03
@Author: xibei
'''


# 1：一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
#
# import time
# sum_people = 0
# for i in range(10):
#     sex = input('请输入你的性别（m：男，f：女）：')
#     if sex == 'f':
#         age = input('请输入你的年纪：')
#         if 10 <= int(age) <= 12:
#             print('恭喜你加入足球队')
#             sum_people += 1
#         else:
#             print("很抱歉你的年纪不符合我们的要求")
#     else:
#         print("很抱歉你的性别不符合我们的要求")
#     time.sleep(1.5)
# print('足球队现在一共有{}人'.format(sum_people))



# 2：利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序： 冒泡排序：小的排前面，大的排后面。

# a = [1, 7, 4, 89, 34, 2]
#
# for i in range(len(a)):
#     # print(i)
#     b = False
#     for j in range(0, len(a)-1):
#         # print(j)
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#             b = True  # 如果发生交换，就重新赋值b
#     if not b:  # 如果整轮没发生交换 就跳出循环
#         break
# print(a)



# 3： 万科笔试题：
# 有一组用户的登录信息存储在字典 login_ifno 里面，字典格式如下：login_info={"admin":"root","user_1":"123456"}
# key表示用户名，value表示密码，请编写函数满足如下条件：
# 1）设计1个登陆的程序， 不同的用户名和对成密码存在个字典里面， 输入正确的用户名和密码去登陆，
# 2）首先输入用户名，如果用户名不存在或者为空，则一直提示输入正 确的用户名
# 3)当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应， 则提示密码错误请重新输入。
# 4)如果密码输入错误超过三次，中断程序运行。
# 5)当输入密码错误时，提示还有几次机会
# 6)用户名和密码都输入正确的时候，提示登陆成功!''

# login_info = {"admin": "root", "user_1": "123456"}
# while 1:
#     name = input('请输入用户名：')
#     if name in login_info:
#         for i in range(1, 4):
#             pwd = input("请输入密码")
#             if login_info[name] == pwd:
#                 print('登录成功')
#                 break
#             else:
#                 print('密码输入错误，还剩下{}次机会'.format(3-i))
#         break



