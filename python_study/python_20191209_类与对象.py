#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191209_类与对象.py
@Date  : 2019/12/9 0009 11:34
@Author: xibei
'''


'''类'''

'''
# 类的语法
# 1.关键字：class
# 2.使用：
#class 类名：   #类名的规范:不能用关键字，驼峰命名StudPyhotn（首字母大写）
  # 属性：变量
  # 行为：函数
'''



# class SeniorTestingEngineer:  # 高级测试工程师类
#     # 属性
#     work_year = 3
#     salary = 20000
#
#     # 行为
#     def coding(self):  # self 对象本身--》有self标记为对象函数，只能对象来调用。self是变量，也可以用其他a，b等
#         print('self:{}'.format(self))
#         print('会写代码')
#
#     def do_sql(self):
#         print('会操作数据库')
#
#     def do_linux(self):
#         print('会使用linux系统')
#
#     def do_funtion_testing(self):
#         print('会功能测试')
#
#     def do_api_test(self):
#         print('会接口测试')





'''
# 1. 创建对象：类名（）
# 2. 对象拥有类里面的所有属性和函数的使用权
# 3. 类里面的函数只能有对象来调用
# 4. 类里面的属性可以对象或类名调用
'''


# p_1 = SeniorTestingEngineer()  # 创建对象
# # 属性和行为的调用
# print(p_1.work_year)
# print(p_1.salary)
# p_1.coding()
# p_1.do_funtion_testing()


# p_2 = SeniorTestingEngineer  # p_2 不是对象
# print(p_2.salary)  # 类名调用
# print(p_2.work_year)  # 类名调用
# # p_2.coding()  # 非对象调用，报错
# # p_2.do_funtion_testing() # 非对象调用，报错
#
# # 非对象调用的时候 需传入对象
# p_2.coding(SeniorTestingEngineer())
