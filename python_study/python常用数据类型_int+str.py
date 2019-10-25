#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python常用数据类型.py
@Date  : 2019/10/11 0011 10:57
@Author: xibei
'''

'''
 Python常用数据类型：数字，字符串，数组，字典，元组
'''

''' 数字 '''
# # 数字： 整数（int）,浮点数（float）
# # 整数
# a = 10
# # 浮点数
# b = 10.01
# # type() 判断数据类型
# print(type(a))
# print(type(b))
# # 强制转换
# print(type(int(b)))
# print(type(float(a)))


''' 字符串 '''
# 定义：成对的单引号、双引号、三引号 括起来的都是字符串

# 字符串的元素：当个字符算一个元素

'''1）索引'''
# 索引：正向编号，从0开始（0，1，...）
#      反向编号，从-1开始（-1，-2，...）
# a = 'python'
# print(a[0])
# print(a[-1])

'''2)切片'''
# 切片：字符串名[索引头:索引尾：步长]
# 注意：取头不取尾，不输入步长默认步长为1
# print(a[0:3])
# print(a[-1:-6:-2])

'''3）字符串的格式化输出'''

# 方式一：占位符 %s string ，%d 整数，%f 浮点数

# name = '溪贝'
# class_id = 12
# course = 'python'
# age = 18
# salary = 15000
# print('''========溪贝INFO======
# 姓名是：%s
# 班级是：%s,%d
# 年龄是：%d
# 期望薪资是：%d''' % (name, course, class_id, age, salary))

# 方式二 format{} 格式化输出
# {}不指定数据类型，按顺序根据花括号去赋值
# 指定顺序的时候，要么都指定要么都不指定

# print('''========溪贝INFO======
# 姓名是：{0}
# 班级是：{2}{1}
# 年龄是：{3}
# 期望薪资是：{4}'''.format(name, class_id, course, age, salary))


'''4）字符串的拼接'''

# 方式一： 字符串的拼接 + （只能是字符串和字符串拼接）
# s_1 = '我的名字是'
# s_2 = '溪贝'
# print(s_1+s_2)

# 方式二： 不同参数之前用逗号隔开
# print(s_1, s_2, '我是python小白')

'''5）字符串的常见内建函数'''

'''str.find()'''
# 查找某个字符 字符串.find（你指定的字符或字符串)
# s = '明天，你好！'
# print(s.find('@'))  # 如果没有找到返回 -1
# print(s.find('好'))  # 传入单个字符 如果找到了 返回索引
# print(s.find('你好'))  # 传入的是字符串，如果找到了 就返回第一个字符所在的索引位置

'''str.replace()'''
# 字符串的替换 字符串.replace(目标，最终替换成什么)
# s = '明天，你好！'
# new_s = s.replace('明天', '溪贝')  # 替换后的字符串需要存起来 或覆盖
# print(new_s)

'''str.split()'''
# 切割 字符串.split() # 返回的数据类型是列表
# s = '明天，你好！'
# value_1 = s.split()
# print("切割后的结果是{}".format(value_1))
# value_2 = s.split('，')
# print('切割后的结果是{}'.format(value_2))

'''str.strip()'''
# 去除指定字符 字符串.strip() # 去掉头尾指定的字符或字符串
# s = '   明天，你好!'
# print(s)
# print(s.strip(' '))
# print(s.strip('!'))
# print(s.strip('你'))  # 不能去掉中间字符
# print(s.strip('好!'))

'''str.upper()'''
