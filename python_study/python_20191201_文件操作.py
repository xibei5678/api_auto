#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191201_文件操作.py
@Date  : 2019/12/2 0002 17:01
@Author: xibei
'''


''' 文件操作 '''


''' 新建文件 '''
# os.mkdir
import os
# os.mkdir('python_12')

# 注意：支持相对 绝对路径
#      不能跨级新建，新建目录前上一级必须存在

''' 删除文件'''
# os.rmdir
# import os
# os.rmdir('python_12')

# 注意：支持相对 绝对路径
#      不可以跨级删除，删除的目录必须是空的


'''获取文件路径'''

# os.getcwd()  # 获取当前的工作路径 具体到目录
# os.path.realpath(__file__)  # 获取当前的工作路径 具体到文件

# realpath == abspath

import os
print(os.getcwd())  # D:\test\python_12_xibei\python_study
print(os.path.realpath(__file__))  # D:\test\python_12_xibei\python_study\python_20191201_文件操作.py

print(os.path.abspath(__file__))  # D:\test\python_12_xibei\python_study\python_20191201_文件操作.py