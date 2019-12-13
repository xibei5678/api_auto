#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191213_类的继承.py
@Date  : 2019/12/13 0013 10:46
@Author: xibei
'''


class RobtOne:  # 一代机器人类

    def __init__(self, name, birthday):
        self.name = name  # 姓名
        self.birthday = birthday  # 出产日期

    def walk(self):
        print('{}会直线行走'.format(self.name))

    def jump(self):
        print('{}会跳跃'.format(self.name))

    def talk(self):
        print('{}会简单的问候'.format(self.name))

    @staticmethod
    def sing(song_name):
        print("会唱{}歌".format(song_name))


# r_1 = RobtOne('rob', '20191210')
# r_1.walk()
# r_1.jump()
# r_1.talk()
# r_1.sing('听妈妈的话')
# print('{}的生日为{}'.format(r_1.name, r_1.birthday))


# 现研究了二代机器人 ，有新的属性和功能：性别和会握手
# 故我们可以继承一代机器人的类，在其基础上添加


'''
  # 继承
# 1.子类拥有父类所有的属性和行为
# 2.父类已存在的函数，再写为重写
# 3.父类没有的函数，叫拓展
# 4.子类自己有的就用自己的，没有就用父类的
'''

class RobtTwo(RobtOne):  # RobtOne 为 RobtTwo的父类，RobtTwo拥有父类所有的属性和行为

    # 重写初始化函数：父类已存在的函数，再写为重写
    def __init__(self, name, birthday, sex):
        self.name = name
        self.birthday = birthday
        self.sex = sex

    # 拓展 ：父类没有的函数，叫拓展
    def handshake(self):
        print("{}会握手".format(self.name))


# r_2 = RobtTwo('rob', '20191210', '女')
# r_2.walk()
# r_2.jump()
# r_2.talk()
# r_2.sing('听妈妈的话')
# r_2.handshake()
# print('{}的生日为{}'.format(r_2.name, r_2.birthday, r_2.sex))



''' 超继承 '''

#1. 在原有的函数基础上再增加
#2. 关键字super
#3.使用： super（子类名，self）.方法名（参数）


class RobtThree(RobtOne):  # RobtOne 为 RobtThree的父类，RobtTwo拥有父类所有的属性和行为

    # 超继承
    def __init__(self, name, birthday, sex):
        super(RobtThree, self).__init__(name, birthday)
        self.sex = sex

    # 拓展
    def handshake(self):
        print("{}会握手".format(self.name))

    # 超继承
    def talk(self, content):
        super(RobtThree, self).talk()
        print('内容如下：{}'.format(content))

#
# r_3 = RobtThree('heby', '20191210', '女')
# r_3.walk()
# r_3.jump()
# r_3.talk('你好')
# r_3.sing('听妈妈的话')
# r_3.handshake()
# print('{}的生日为{}'.format(r_3.name, r_3.birthday, r_3.sex))


''' 多继承 '''

# 1.圆括号中继承父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
# 2.支持多层父类继承，子类会继承父类所有的属性和方法，包括父类的父类的所有属性 和 方法。


# class Human:
#     def __init__(self, sex):
#         self.sex = sex
#
#     def p(self):
#         print("这是Human的方法")
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def p(self):
#         print("这是Person的方法")
#
#     def person(self):
#         print("这是我person特有的方法")

#
# class Teacher(Person):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#
# class Student(Human, Person):
#     def __init__(self, name, sex, grade):
#         Human.__init__(self, sex)
#         Person.__init__(self, name)
#         self.grade = grade
#
#
# class Son(Human, Teacher):
#     def __init__(self, sex, name, age, fan):
#         Human.__init__(self, sex)
#         Teacher.__init__(self, name, age)
#         self.fan = fan


# ******创建对象********

# stu = Student("tom", "male", 88)
# print(stu.name, stu.sex, stu.grade)
# stu.p()  # 虽然父类Human和Person都有同名P()方法 ，但是调用的是括号里的第一个父类Human的方法
#
# son1 = Son("jerry", "female", 18, "打球")
# son1.person()  # 可以调用父类的父类的方法。
# son1.p()  # 子类调用众多父类中同名的方法，按继承的顺序查找。


''' 多继承注意 '''

# 1.子类中未重写初始化函数，会按顺序继承父类一的属性，创建对象时，需按照父类一进行传参，故当调用父类二中存在有属性值的利用时会报错
# 2. 多继承时，init函数尽量重写，保证调用方法时不出错
# 3.重写时，可直接使用类名.init方法调用，或者使用super（）.init 调用

class Hu:
    def __init__(self, sex):
        self.sex = sex

    def p(self):
        print("这是Human的方法")

    def str_1(self):
        print('sex为：{}'.format(self.sex))


class Pe:
    def __init__(self, name):
        self.name = name

    def p(self):
        print("这是Person的方法")

    def person(self):
        print("这是我person特有的方法")

    def str_2(self):
        print('姓名为：{}'.format(self.name))


class St(Hu, Pe):
    def study(self):
        print('这是我student的方法')


# s = St('男')
# # s = Student('男', 'lemon') # 因student继承了human，只需传入一个参数sex，故会报错
# s.p()
# s.person()
# s.study()
# s.str_1()
# # s.str_2() # 因student继承了human，无name属性，故会报错