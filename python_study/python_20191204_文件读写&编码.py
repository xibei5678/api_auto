#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191204_文件读写&编码.py
@Date  : 2019/12/4 0004 11:23
@Author: xibei
'''


'''文件操作'''

import os

# 打开文件
# open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
# 参数file:文件路径
# 参数mode：文件的模式，默认为只读（r），常用的有：r(只读)，w(只写)，a（追加），r+（读写）,w+（读写）,a+（读写）
# 参数 encoding ：编码


'''文件模式'''

# r: 只读模式(文件需已存)
# w：只写模式，如果文件存在便清除内容，如果未存在便新建
# a：追加，如果文件存在便追加，如果未存在便新建
# r+：读写模式（文件需已存在），读写会根据光标的位置（默认位置是0.0）进行读写内容，写入是如果有内容会覆盖写
# w+：读写，已存在的文件，会先清空内容再进行读写，同样读写都是根据光标位置开始。（故出现不管先写入还是先读取操作，读取内容都为空）
# a+：读写，读写都会从文末开始进行，故读取无内容


'''文件常用操作函数'''
# file.write() 写入内容
# file.writelines() 多行写入，参数需以list传入的字符串，字符串中需带有“\n”换行符才会写入后会换行
# file.read()  读取全部内容
# file.readline() 读取一行内容
# file.readlines() 读取多行
# file.tell()
# file.seek(位移数，相对位移的位置) 光标的偏移
# file.closed 文件是否关闭 （开：false，关：true）
# file.close() 关闭文件

'''上下文管理区'''

# with open() as file:  # 这样打开文件操作完会自动关闭文件
#     文件操作如：
#     file.read()
#     file.write()
#     等

'''实操'''
# 先新建一个“python_01.txt”

# file = open('python_01.txt', 'r', encoding="utf-8")  # 返回相当于句柄需接收
# print(file.read())
# file.write('啦啦')
# file.writelines(['hello python\n','python_12 lemon\n'])
# print(file.read())
# file.write('lemon')
# print(file.read())
# print(file.readline())
# print(file.tell())
# file.seek(0, 0)  # 移动光标到开头
# print(file.readlines())
# print(file.closed)
# file.close()
# print(file.closed)


'''编码'''

# 1. 为了处理英文字符，产生了ASCII码
# 2. 为了处理中文字符，产生了GB2312
# 3. 为了处理各国字符，产生了Unicode
# 4. 为了提高Unicode存储和传输性能，产生了UTF-8,它是unicode的一种实现方式

# 备注： 系统一般编码都为unicode


# test = '你好呀'
# print(test.encode('GBK'))  # 编码
# print(test.encode('GBK').decode('GBK'))  # 解码

# test = 'hello python'
# print(test.encode('ASCII'))  # 编码
# print(test.encode('ASCII').decode('ASCII'))  # 解码

