#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191125_函数练习.py
@Date  : 2019/11/25 0025 17:50
@Author: xibei
'''

# 1：一个足球队在寻找年龄在x岁到y岁的小女孩（包括x岁和y岁）加入。编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数。
#
# def football_people(k,x,y):
#     for i in range(k):
#         sex = input('请输入你的性别（女：f，男：m）：')
#         age = input('请输入你的年龄：')
#         count = 0
#         if sex == 'f' and x <= int(age) <= y:
#             print("恭喜你加入足球队")
#             count += 1
#         else:
#             print('对不起，你不符合要求')
#
#     print('足球队目前一共{}人'.format(count))
#
# football_people(3,12,15)



# 2：写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5

#
# def check_len(a):
#     if len(a) >= 5:
#         print('{}的长度大于5'.format(a))
#     else:
#         print('{}的长度小于5'.format(a))
#
# check_len((1,2,3))


# 3、写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
#
# def check_list(l):
#     if l is list and len(l) > 2:
#         del l[2:]
#     else:
#         print('格式错误,不是列表')
#     print(l)
#
# check_list('python')

# 4、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典。
#
# def check_dict(d,s):
#     if s not in d.values():
#         if s in d.keys():
#             d[s+'_01'] = s
#         else:
#             d[s] = s
#     else:
#         print('字符串是字典的值')
#     print(d)
#
# check_dict({'name': '溪贝', "sex": "女"}, 'name')
