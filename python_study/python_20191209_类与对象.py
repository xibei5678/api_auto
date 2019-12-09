#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191209_类与对象.py
@Date  : 2019/12/9 0009 11:34
@Author: xibei
'''


'''类'''

# 类的语法
# 1.关键字：class
# 2.使用：
#class 类名：   #类名的规范： 不能用关键字，驼峰命名StudPyhotn（首字母大写）
  # 属性：变量
  # 行为：函数



class SeniorTestingEngineer:  # 高级测试工程师类
    # 属性
    work_year = 3
    salary = 20000

    # 行为
    def coding(self):  # self 对象本身--》对象函数，只能对象来调用
        print('self:{}'.format(self))
        print('会写代码')

    def do_sql(self):
        print('会操作数据库')

    def do_linux(self):
        print('会使用linux系统')

    def do_funtion_testing(self):
        print('会功能测试')


# 1. 创建对象：类名（）
# 2. 对象拥有类里面的所有属性和函数的使用权
# 3. 类里面的函数只能有对象来调用

