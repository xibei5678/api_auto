#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20200408_反射.py
@Date  : 2020/4/8 0008 10:20
@Author: xibei
'''

'''python 的反射'''



'''getattr(object,name[,default])函数'''
#  获取对象 object 的属性或者方法，若存在则打印出来；若不存在，则打印默认值，默认值可选。
# 注意：object 为对象名，不需要实力，在调用对象方法的时候需要实例化。
#      如果返回的是对象的方法，那么打印的结果是方法的内存地址。如果需要运行这个方法，那么可以在后面添加括号 () 。



class function_demo(object):
    name = 'demo'

    def run(self):
       return "hello function"


print(getattr(function_demo, "name"))  # 获取 name 属性，存在就打印出来--- demo
print(getattr(function_demo, 'run'))  # 获取 run 方法，存在打印出方法的内存地址
print(getattr(function_demo, 'age', '不存在'))  # 获取 age 属性，不存在就打印默认值出来--- 不存在
print(getattr(function_demo(), "run")())  # 调用run方法，对象需要实例化


'''hasattr(object,name) 函数'''
# 判断一个对象里面是否有 name 属性或者 name 方法，返回 bool 值，如果有 name 属性（方法）则返回 True ，否则返回 False 。
# 注意： name 需要使用引号括起来。

print("*"*50)
print(hasattr(function_demo, "name"))  # 判断对象是否有 name 属性，True
print(hasattr(function_demo, "run"))  # 判断对象是否有 run 方法，True
print(hasattr(function_demo, "age"))  # 判断对象是否有 age 属性，False


'''setattr(object,name,values) 函数'''
# 给对象的属性赋值，若属性不存在，则先创建再赋值。

print("*"*50)
print(hasattr(function_demo, "age"))  # 判断 age 属性是否存在，返回False
setattr(function_demo, "age", 18)  # 创建 age属性并赋值
print(hasattr(function_demo, "age"))  # 判断 age 属性是否存在，返回True
print(getattr(function_demo, "age"))  # 获取 age 属性值，18


'''delattr(object,name)函数'''
# 删除对象的属性

print("*"*50)
print(hasattr(function_demo, "age"))  # 判断 age 属性是否存在，返回True
delattr(function_demo, "age")  # 创建 age属性并赋值
print(hasattr(function_demo, "age"))  # 判断 age 属性是否存在，返回False
delattr(function_demo, "run")  # 只支持删除属性，不能删除方法，故报错：AttributeError: run （没有run属性）

