#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191210_类的调用.py
@Date  : 2019/12/10 0010 16:16
@Author: xibei
'''


# class SeniorTestingEngineer:  # 高级测试工程师类
#     # 属性
#     work_year = 3
#     salary = 20000
#
#     # 行为
#     def coding(self):  # 对象方法
#         print('self:{}'.format(self))
#         print('会写代码')
#         print(self.work_year)
#
#     @staticmethod
#     def do_sql():  # 静态方法,没有self参数，可以非对象调用，类名.方法 进行调用，不需要特地创建对象调用
#         print('会操作数据库')
#         # print(self.work_year)  # 不支持属性调用，不使用类属性的方法可以写成静态方法
#
#     @classmethod  # 类方法，由cls参数标记
#     def do_linux(cls):  # 类方法
#         print('cls为：{}'.format(cls))
#         print('会使用linux系统')
#         print(cls.work_year)  # 类属性调用 ，不支持self.属性调用



'''区别'''

# 1.对象方法：有self参数，只能有对象调用
#           对象方法中可直接通过self.属性 调用类的属性
# 2.静态方法：由@staticmethod装饰器，无self参数，可以对象或类名调用
#           静态方法中不可直接通过self.属性 调用类的属性
# 3.类方法：由@classmethod装饰器，且有cls参数标记，可以对象或类名调用
#           类方法中可直接通过cls.属性 调用类的属性
# 4. 三种方法中都可以有：位置参数、默认参数、动态参数、关键字参数


'''类的方法调用'''

# p_1 = SeniorTestingEngineer()  # 创建对象
# print(p_1.work_year)
# print(p_1.salary)
# p_1.coding()
# p_1.do_sql()
# p_1.do_linux()

# P_2 = SeniorTestingEngineer  # 类名
# print(P_2.work_year)  # 类名调用属性
# print(P_2.salary)  # 类名调用属性
# P_2.do_sql()  # 静态方法支持类名调用
# P_2.do_linux()  # 类方法支持类名调用
# # P_2.coding()  # 对象方法不支持类名调用


'''类中的方法相互调用'''

# class SeniorTestingEngineer:  # 高级测试工程师类
#     # 属性
#     work_year = 3
#     salary = 20000
#
#     # 行为
#     def coding(self):  # 对象方法
#         print('会写代码')
#
#         # self.do_linux()  # 类方法调用
#         # self.do_sql()  # 静态方法调用
#
#     @staticmethod
#     def do_sql():
#         print('会操作数据库')
#         # SeniorTestingEngineer().coding()  # 对象方法调用
#         # SeniorTestingEngineer().do_linux()  # 类方法调用
#
#
#     @classmethod  # 类方法，由cls参数标记
#     def do_linux(cls):  # 类方法
#         print('会使用linux系统')
#
#         cls().coding()  # 对象方法调用
#         cls.do_sql()  # 静态方法调用


# p = SeniorTestingEngineer()  # 创建实例

# p.coding()  # 测试 类方法和静态方法 调用

# p.do_sql()  # 测试 对象方法和类方法 调用

# p.do_linux()  # 测试 对象方法和静态方法 调用


