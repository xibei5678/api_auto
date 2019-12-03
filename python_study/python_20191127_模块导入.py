#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191127_模块导入.py
@Date  : 2019/12/3 0003 10:55
@Author: xibei
'''


''' 模块导入 '''

'''
import..  # 具体到模块，函数调用： xxx模块名.函数
import...as.. # as 意为重命名 调用样式:重命名.函数
from...import...as...
from...import...  # 具体到模块且必须到模块，或到函数
from ... import * # 
'''

# 假如有个文件路径如下‘D:\test\python_12_xibei\python_study\test\lemon\test_function.py’，
# test_function 里有函数sub（）和add（）

'''导入示例'''

# import python_study.test.lemon.test_function
# python_study.test.lemon.test_function.sub()
# python_study.test.lemon.test_function.add()
#
# import python_study.test.lemon.test_function as suanfa
# suanfa.add()
# suanfa.sub()
#
# from python_study.test.lemon import test_function
# test_function.sub()
# test_function.add()
#
# from python_study.test.lemon.test_function import sub
# sub()

# from python_study.test.lemon.test_function import *
# sub()
# add()


'''错误示范'''
# from python_study.test.lemon import *  # import前未具体到模块

# from python_study.test import lemon.test_function # import后未具体到模块


'''相对路径 绝对路径'''

# 相对路径：在同一级别下 如：open（'text.txt'）会默认在python_20191127_模块导入文件的同一级别找
# 绝对路径：如：D:\test\python_12_xibei\python_study\python_20191127_模块导入.py  为绝对路径


'''本地库或安装的第三方库 导入时可直接输入模块名，默认在当前目录下找，找不到会到python配置的环境变量下找'''

