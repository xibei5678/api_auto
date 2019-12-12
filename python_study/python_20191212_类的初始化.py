#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191212_类的初始化.py
@Date  : 2019/12/12 0012 10:42
@Author: xibei
'''


'''初始化函数'''
# 1. 作用：在创建对象的时候，设置初始值(属性参数化)
# 2.用法：def __init__(self,参数1，参数2...)
# 3. 有初始化函数的类，创建对象时需传参


# class SeniorTestingEngineer:  # 高级测试工程师类
    # # 属性
    # work_year = 3
    # salary = 20000

    # 初始化函数

    # def __init__(self):  # 无参数
    #     self.name = 'lemon'
    #     self.work_year = 3
    #     self.salary = 20000

    # def __init__(self, name, work_year, salary):  # 有传参
    #     self.name = name  # 将属性赋值给对象
    #     self.work_year = work_year
    #     self.salary = salary
    #
    # # 行为
    # def coding(self, language):  # 对象方法
    #     print('{}同学，工作{}年，月薪{}，会写{}代码'.format(self.name, self.work_year, self.salary, language))
    #
    # @staticmethod
    # def do_sql():
    #     print('会操作数据库')
    #
    # @classmethod  # 类方法，由cls参数标记
    # def do_linux(cls):  # 类方法
    #     print('会使用linux系统')


# 初始化函数无参数 创建对象
# p1 = SeniorTestingEngineer()  # 创建对象跟无初始化函数一样 不需要传参
# p1.coding('python')

# p2 = SeniorTestingEngineer()  # 无法对name，work_year,salary 进行参数化
# p2.coding('java')


# 初始化函数有参数 创建对象
# p3 = SeniorTestingEngineer('花花', 5, 10000,)  # 创建对象跟无初始化函数一样 不需要传参
# p3.coding('python')
#
# p4 = SeniorTestingEngineer('lemon', 10, 20000,)  # 可以对name，work_year,salary 进行参数化
# p4.coding('java')


''' _call_ 方法'''

# 1.作用：能够让类的实例对象，像函数一样被调用
# 2._call__()方法还可以带参数


# 有无__call__方法，类的调用

# class Fib(object):
#
#     def __init__(self):
#         print('此处_init_方法')
#
#     # def __call__(self, name, sex):
#     #     print("此处_call_方法")
#     #     print("姓名：{}".format(name))
#     #     print("性别：{}".format(sex))
#
#
# f = Fib()
# print("f为：{}".format(f))

# # 有_call_方法
# f('华华', '女')

# # 无_call_方法
# f('华华', '女')  # 不支持直接调用，故会报错：TypeError: 'Fib' object is not callable



#  _init_方法 和_call_方法参数使用
# 1. init中的参数需创建对象时传入
# 2. call中的参数，在调用时传入和其他方法相同

# class Fib(object):
#
#     def __init__(self, name, sex):
#         print('此处_init_方法')
#         self.name = name
#         self.sex = sex
#         print("self.name:{}".format(self.name))
#         print("self.sex:{}".format(self.sex))
#
#     def __call__(self, name, sex):
#         self.name = name
#         self.sex = sex
#         print("此处_call_方法")
#         print("self.name:{}".format(self.name))
#         print("self.sex:{}".format(self.sex))
#
#
# f = Fib('李梅', '女')  # 创建对象
# f('李雷', '男')  # 类直接调用
