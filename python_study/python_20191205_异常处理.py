#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191204_异常处理.py
@Date  : 2019/12/4 0004 17:20
@Author: xibei
'''



'''异常处理'''

# 1.异常处理机制：抓到异常 然后做出相关处理
# 2.try...except..
# 3.try后面监控觉得可疑的代码，如果出现错误就会进入except，如果未出错便就不进入，继续执行except模块后面的代码
# 4. 可以有多个except，监控多种错误
# 5.一个except 对应处理一个错误类型
# 6.try...except...finally...
   # finally 后面的代码，不管try后面代码是否报错都执行
# 7.try...except...else...
   # else 后面的代码，如果try后面的代码没问题，就会执行，如果有问题就不执行




# try:
#     print(a)  # a未被命名
# except Exception as e:  # 处理（exception）类的错
#     print("出错了：{}".format(e))
# print("啦啦啦啦")


'''Python常见错误类型'''

# 1. BaseException  所有异常的类型
# 2. Exception      常规错误的基类
# 3. IndexError     索引错误
# 4. ImportError    导入模块/对象失败
# 5. IoError        输入/输出操作失败
# 6. AttributeError 对象没有这个属性
# 7. KeyError       映射中没有这个键
# 8. NameError      未声明/初始化对象没有属性
# 9. SyntaxError    python语法错误
# 10.IndentationError 缩进错误
# 11. AssertionError  断言错误



'''示例'''


# 只处理一种异常

# a = 10
# c = [1, 2, 3, 4]
# try:
#     print(a+b)  # 会出现NameError错误,因为b未被声明
# except IndexError as e:  # 只处理 指定类型indexerror的错误
#     print("报错了：{}".format(e))


# 处理多种异常

# a = 10
# # b = 2
# c = [1, 2, 3, 4]
# try:
#     print(a+b)  # 会出现NameError错误,因为b未被声明
#     print(c[4]) # 会出现indexerror错误,因为索引超出范围
# except (NameError,IndexError) as e:  # 处理NameError,IndexError错误
#     print("报错了：{}".format(e))


# a = 10
# # b = 2
# c = [1, 2, 3, 4]
# try:
#     print(a+b)  # 会出现NameError错误,因为b未被声明
#     print(c[4]) # 会出现indexerror错误,因为索引超出范围
# except NameError as e:  # 处理NameError错误
#     print("报错了：{}".format(e))
# except IndexError as e:  # 处理IndexError错误
#     print("报错了：{}".format(e))


# try...except...finally...

# a = 10
# # b = 2
# try:
#     print(a+b)  # 会出现NameError错误,因为b未被声明
# except NameError as e:  # 处理NameError错误
#     print("报错了：{}".format(e))
# finally:
#     print("测试结束")  # 不管是否报错都会执行此代码


# try...except...else...

# a = 10
# # b = 2
# try:
#     print(a+b)  # 会出现NameError错误,因为b未被声明
# except NameError as e:  # 处理NameError错误
#     print("报错了：{}".format(e))
# else:
#     print('b为{}'.format(b))  # 如果try后面代码没报错会执行此代码

