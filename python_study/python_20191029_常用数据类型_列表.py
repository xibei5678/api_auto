#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python常用数据类型_列表.py
@Date  : 2019/10/29 0029 17:26
@Author: xibei
'''


''' 列表 list []'''

'''
# 1: 可以有空列表
# 2：元素直接用逗号隔开
# 3：列表内什么类型的数据都可以放
# 4： 取单个元素 列表名[索引值]   索引从0开始（从左到右，从右到左从-1开始） 
# 5: 支持切片，同字符串操作
# 6： 列表中还可以嵌套放列表
# 7: 列表支持 增删改查
'''

L = [1, 0.02, 'sunflower', ('sunny', 33, '薄荷糖'), [7, 6, 8]]

'''   常用函数     '''

'''1.添加元素'''
# list.append() # 在列表的最后添加元素，每次只能添加一个
# L.append('hello,everyone')
# print(L)

# list.insert(索引，值) # 根据索引位置，插入
# L.insert(0, 'hello')
# print(L)

'''2. 删除'''
# list.pop() 默认删除最后一个值 并返回删除值
# print(L.pop())
# print(L)

# list.pop(索引) 根据索引进行删除 并返回删除值
# print(L.pop(3))
# print(L)

'''3. 修改'''  # 列表名[索引]= 值
# L[1] = '零点零2'
# print(L)

'''4. 排序'''

# list.sort() 排序:从小到大，针对数字
# print(L[-1].sort()) # 无返回值
# print(L[-1])
# print(L[-1].sort(reverse=True))  # 从大到小
# print(L[-1])

# list.reverse() 倒序 无返回值
# print(L.reverse())
# print(L)

''' 扩展 '''
# list.count() # 统计某个元素个数
# list_1 = [1, 2, 3, 4, 5, 6]
# print(list_1.count(1))

# list.index() # 查找某个元素 返回元素索引 未找到报错
# list_1 = [1, 2, 3, 4, 5, 6]
# print(list_1.index(6))

# list.clear() # 清除所有的元素
# list_1 = [1, 2, 3, 4, 5, 6]
# list_1.clear()  # 无返回值
# print(list_1)

# list.copy()  # 拷贝
# list_1 = [1, 2, 3, 4, 5, 6]
# list_2 = list_1.copy()
# print(list_2)
#
# list_3 = list_1  # copy与赋值（=）的不同：copy直接拷贝不同的内存地址，赋值指向同一内存地址
# print(id(list_1))
# print(id(list_2))
# print(id(list_3))
#
# list_3.pop()
# print(list_3)
# print(list_1)  # list_1会根据list_3改变而改变

# list.extend() # 把两个列表 放到一块
# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_1.extend(list_2)
# print(list_1)

# list.remove() # 根据指定的值删除 每次只会删除一个
# list_1 = [1, 2, 3, 2, 4, 2, 5, 6]
# list_1.remove(2)
# print(list_1)
#
# list_1.remove(2)
# print(list_1)
#
# list_1.remove(2)
# print(list_1)




