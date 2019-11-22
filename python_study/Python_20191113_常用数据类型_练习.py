#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : list_tuple_str_练习.py
@Date  : 2019/11/12 0012 11:47
@Author: xibei
'''



'''列表'''
# 1：L = [ ['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]
#    打印Apple、Python、Lisa

# L = [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]
# print(L[0][0], L[1][1], L[2][2])


#
# 2：完成列表a=[1,7,4,89,34,2]的冒泡排序（冒泡排序：小的排前面，大的排后面。），
#    并写出冒泡的原理是什么？（很重要）

# a = [1, 7, 4, 89, 34, 2]   冒泡排序：每一位元素依次比对，如1和7对比，1和4对比，1和89对比，1和34对比，1和2对比 然后再循环7和4对比....
# a = [1, 2, 4, 7, 99, 89]
# for i in range(len(a)):  # 对比轮次
#     status = False  #  标记是否交换，如果一轮没交换数据直接退出循环
#     print(i)
#     for j in range(1, len(a)-1):  # 元素依次对比
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#             status = True
#     print(status)
#     if not status:
#             break
# print(a)

#
# 3：利用input函数从控制台获取一个当前日期，
#    如：20181031,然后利用自己所学知识，
#    把他转换成 "2018年10月31号".

# a = input('请输入当前日期(格式如：20181031):')
# print('{}年{}月{}号'.format(a[:4], a[4:6], a[6:8]))


''' 字典 '''

# 有一个字典： {"广东":["深圳","广州","阳江"], "湖南":["长沙","益阳","怀化"], "湖北":["武汉","襄阳","黄冈"]}
# 你从控制台输入一个省份
# 根据你的省份判断 你可以选择哪些城市
# 当你选择完毕后，就打印一个信息到控制台，告诉你，你选择了XX省份XX城市 #如果省份不存在 或者是城市不存在 那么就告诉你 你输入错误 终止程序
# d = {"广东": ["深圳", "广州", "阳江"], "湖南": ["长沙", "益阳", "怀化"], "湖北": ["武汉", "襄阳", "黄冈"]}
# s = input('请输入省份：')
# if s in d.keys():
#     c = input('请输入城市：')
#     if c in d[s]:
#         print('你选择了{}省{}城市'.format(s, c))
#     else:
#         print('输入错误')
# else:
#     print('输入错误')
