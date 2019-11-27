#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191125_函数.py
@Date  : 2019/11/25 0025 14:52
@Author: xibei
'''


''' 函数 '''



# 语法：
'''
def 函数名（参数列表）：
    代码块
    return 变量的个数
'''
# 关键字 def define 定义
# 参数列表：位置参数、默认参数、动态参数、关键字参数 ，参数个数可为0也可以为多个，多个参数直接用逗号隔开
# return 变量的个数 也可以为0，也可以为多个，多个变量之间用逗号隔开
# return的作用：当你调用函数的时候 返回一个结果 并代表函数终止
# 参数 默认是根据顺序赋值，如果不想按照顺序赋值，可以指定关键字，但关键必须跟参数保持一致

'''示例'''
# def greet_user():  # 参数为0个
#     print('同学们晚上好！')
#     return  # 返回变量为0 ,函数返回默认为none，可以不写return
#
# greet_user()
# print(greet_user())
#
#
#
# def greet_user_01(name):  # 行参/位置参数，调用的时候必须要传，但代码块可以不用
#     print('{}同学晚上好呀！！！'.format(name))
#     return 1
#
# greet_user_01('篮子')
# print(greet_user_01('篮子'))
#
#
# def greet_user_02(name, content='学习还习惯嘛？'):  # 默认参数，必须放在位置参数后面
#     print('{}同学晚上好呀,{}'.format(name, content))
#     return name, content
#
# greet_user_02('篮子')
# greet_user_02('篮子', '最近还好嘛？')
# print(greet_user_02('篮子', '最近还好嘛？'))  # 多个变量返回元组的形式
#
#
#
# def greet_user_03(name='溪贝', content='学习还习惯嘛？'):  # 多个默认参数
#     print('{}同学晚上好呀,{}'.format(name, content))
#
# greet_user_03('最近还好嘛？', '篮子')  # 默认是按顺序传参
# greet_user_03(content='最近还好嘛？', name='篮子')  # 关键字参数 根据关键字传参
# print(greet_user_03('最近还好嘛？', '篮子'))


'''练习'''

# 写一个函数 计算1-100的整数和 要求返回最后的结果值

# def sub(a, b):
#     total = 0
#     for i in range(a, b):
#         total += i
#     return total
#
# print(sub(1,101))


'''动态参数'''
# 动态参数又叫不定长参数，不定参数个数，想输入几个就输入几个
# 动态参数：*变量名 ，变量名一般使用args（args = arguments）

# def coding(*args):  # 这是一个显示所用编程语音的函数
#     print(args)  # 不定长参数变成元组
#
# coding('python','java','shell','c','php')


'''关键字参数'''

#  关键字参数： **变量名，变量名一般为kwargs(key word arguments)
# 可以接受多个任意 键值对

# def students_msg(**kwargs):
#     print(kwargs)  # 键值对参数变成字典
#
# students_msg(name='溪贝', sex='女', age='18')


''' 混合使用'''
# 一般使用顺序：位置参数、动态参数、默认参数、关键字参数 （使用和赋值时保持这个顺序不容易出错）

# def student_info(name,*subject,age=18,**kwargs):
#     print(name)
#     print(subject)
#     print(age)
#     print(kwargs)

# student_info('花花','python','java','c','rub',age=20,sex ='女',interest='唱歌')
# student_info(age=20,sex ='女',interest='唱歌','花花','python','java','c','rub') # 错误示范 （原因：按顺序赋值）
# student_info(age=20,kwargs={'sex' :'女','interest':'唱歌'},name='花花',subject=('python','java','c','rub'))
#  错误示范 （原因：动态参数用关键字进行赋值不了，关键字赋值可以对位置参数、默认参数和关键字参数）
