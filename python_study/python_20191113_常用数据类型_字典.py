#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python常用数据类型_字典.py
@Date  : 2019/11/13 0013 15:18
@Author: xibei
'''

''' 字典 '''

# 1. dict {}
# 2. 字典是无序的
# 3. 字典的值都是key：value成对存在
#     value:可以是任意类型
#     key：不可变，不支持列表、字典，可以为数字、字符串、元组
# 4. key 一般常用的都是字符串
# 5. 键值对 不同的键值对直接用逗号隔开
# 6. 字典可变 支持增删改查
# 7. key 必须是唯一的

d = {'class_id': 'python12', 'num': 104, 'grade': [99, 100, 45, 66]}

'''查询'''  # 根据key查询 字典名[key]

# print('班级：', d['class_id'])
# print('成绩中的第二位：', d['grade'][1])

# 查询所有的key    字典名.keys() 返回一个集合
# 查询所有的value  字典名.values()  返回一个集合
# 查询所有的键值对  字典名.items()  返回一个集合

# print(d.keys())
# print(d.values())
# print(d.items())


'''删除'''
# 字典名.pop(key)  指定删除 返回被删除的value
# 字典名.popitem() 随机删除 返回key，value的元组
# 字典名.clear()   清空  无返回值

# print(d.pop('class_id'))

# print(d.popitem())
# print(d)

# d.clear()


'''修改和新增'''  # 字典名[key]=value

# 修改 ：key 是已存在的
# 新增： key 不存在
# 如果key已存在，就是修改。如果key不存在就新增

# d['student'] = ['花花', '莉莉']  # 新增
# print(d)

# d['class_id'] = 'lemon_python_12'  # 修改
# print(d)

''' 常见函数 '''

# 字典名.get(key) 等同于字典[key]
# print(d.get('class_id'))

# 字典名.copy()  拷贝
# d_1 = d.copy()
# print(d_1)

# dict.fromkeys(keys,默认的值) # values为空是值为none

# d_2 = {}
# d_2 = d_2.fromkeys(('class_id', 'name', 'sex'))
# d_2 = d_2.fromkeys(('class_id', 'name', 'sex')，10)
# print(d_2)

# 字典名.setdefault(key,设置的值) 和 get()方法 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。

# d_3 = d.setdefault('class_id', 'lemon_python_12')
# d_4 = d.setdefault('name', 'lemon_python_12')
# print(d_3)
# print(d_4)  # 返回查询或设置的值
# print(d)  # 查询的key不存在，会新增并修改原字典
