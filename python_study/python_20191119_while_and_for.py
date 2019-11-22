#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191119_whlie_and_for.py
@Date  : 2019/11/19 0019 11:17
@Author: xibei
'''


''' 循环语句 '''

#  重复的做某件事
#  执行循环：触发条件
#  终止循环： 终止条件 如果没有的话 就不能停止 死循环

''' while 循环'''

# 语法： while 条件表达式：  #（条件表达式：比较运算符、逻辑运算、成员运算、数据 非空和空的情况）
#             要循环的代码/循环体/执行的语句

# 用法： while 后面的表达式成立（True） 那么就执行 不成立（False）就不执行
# 重点： 每次执行完成后，会重新来判断while后的条件 再决定是否循环

# 破解死循环： 设置终止条件
# 1） break ：终止循环 （while和break的结合使用，遇到break就终止循环）
# 2） 加一个终止条件
# count = 1  # 终止条件
# while count < 10:
#     print('我是while 循环语句的第{}次循环'.format(count))
#     count += 1
# 3）技巧：尽量不要while后一直是true，如比较运算结果是可变的（如上方count的值）


# 利用while 循环 完成1-100的整数相加
# a = 1
# b = 0
# while a < 101:
#   b += a
#   a += 1
# print(b)


'''for 循环'''
# 语法： for item in 数据/指定的数据范围：
#           代码块

# 作用：用来遍历元素 （遍历：访问数据中的每一个元素 按顺序挨个访问）
# 不会轻易进入死循环
# for 循环的次数由元素个数决定

# s = 'David zhang'
# s = (1,0.02,'hello',[2,5],('wendy','蓝色火'))
# s = [[1,2],[3,4],[5,6]]
# s = {'name':'小麦','address':'杭州'}
# for item in s:
#     print(item)
# print(s.items())
# for a in s.items():
#     print(a)

''' range 函数 '''
# 语法：range（m,n,k） #m：开头 n：结尾  k：步长
# 特点：取头不取尾，默认步长为1，只有n时，m默认为0

# 用for循环和range函数求1-100的和
# total = 0
# for item in range(1, 101):
#     total += item
# print(total)

'''嵌套循环'''

# list_1 = [['python', 'java', 'c语言'], ['lemon', '51testing', '博为峰'], ['华华', '土豆', '小简']]
# a = 0
# for item in list_1:
#     a += 1
#     print('list_1的第{}个元素为：{}'.format(a, item))
#     for i in item:
#         print('list_1的第{}个元素的子元素：{}'.format(a, i))

# 编写9*9乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}*{}={} '.format(i, j, i*j), end='')  # end='' 不换行输出
#     print('')
