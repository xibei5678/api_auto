#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191201_文件操作.py
@Date  : 2019/12/2 0002 17:01
@Author: xibei
'''


''' 文件操作 '''


''' 新建文件 '''
import os

# os.mkdir
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


# print(os.getcwd())  # D:\test\python_12_xibei\python_study
#
# print(os.path.realpath(__file__))  # D:\test\python_12_xibei\python_study\python_20191201_文件操作.py
#
# print(os.path.abspath(__file__))  # D:\test\python_12_xibei\python_study\python_20191201_文件操作.py



''' 判断是否为文件或目录 '''

# os.path.isdir("文件夹路径")  # 判断该路径是否为目录  是返回true，不是返回false
# os.path.isfile("文件路径")  # 判断该路径是否为文件  是返回true，不是返回false

# file_path = os.getcwd()  # 当前文件的目录：D:\test\python_12_xibei\python_study
# print(os.path.isfile(file_path))
# print(os.path.isdir(file_path))

''' 获取目录或文件名 '''

# os.path.dirname('目录或文件路径')  # 返回上一级目录
# os.path.basename(‘目录或文件路径’)  # 返回当前目录或文件名

# file_path = os.path.realpath(__file__)  # 当前文件的路径：”D:\test\python_12_xibei\python_study\python_20191201_文件操作.py“
# print(os.path.dirname(file_path))  # 返回结果：”D:\test\python_12_xibei\python_study“
# print(os.path.basename(file_path))  # 返回结果：python_20191201_文件操作.py


'''路径拼接'''
# 方法一：”+“ 拼接
# 方法二：os.path.join()

# file_path = os.getcwd()
# print(file_path+'\python_20191201_文件操作.py')
# print(os.path.join(file_path, 'python_20191201_文件操作.py'))
# print(os.path.join(file_path, 'test', 'python_20191201_文件操作.py'))

'''路径切割'''
# os.path.split() #  返回元组
# file_path = os.path.realpath(__file__)
# print(os.path.split(file_path))

''' 获取目录列表'''
# os.listdir(文件目录) # 返回list 相当于命令ll
# print(os.listdir(os.getcwd()))
# 结果为：['python_20191010_安装环境及语法.py', 'python_20191011_常用数据类型_int+str.py'.....]





