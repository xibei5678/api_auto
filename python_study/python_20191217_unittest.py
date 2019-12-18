#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191217_unitest.py
@Date  : 2019/12/17 0017 15:13
@Author: xibei
'''

'''unittest 单元测试'''

# 1. unittest框架 Python自带的
# 2. unittest 用于单元测试 主要的四大类 分别如下：
        # TestCase  写测试用例
        # TestLoader 用例加载
        # TestSuite  测试集
        # TextTestRunner 执行用例&输出报告

# 3. 写用例，需要继承TestCase类，并需要注意：
    # 1）.用例是一个一个的对象方法
    # 2）. 用例test开头，才能被识别
    # 3）.用例里面不能传递参数

# 4.用例加载 ：
    # 方法一： addTest() 添加用例，测试类对象的形式来添加
     #用法：TestSuite().addTest(测试类（测试方法）)

    # 方法二：TestLoader从测试类里面进行添加
            # TestSuite().addTest（TestLoader().LoadTestsFromTestCase(测试类)）
            # TestSuite().addTest（TestLoader().LoadTestsFromModule(测试模块)）

# 5. 装用例：TestSuite

# 6. 执行用例：TextTestRunner 执行用例，以文本形式显示测试结果
    # unitest.TextTestRunner().run(测试集)

# 7. 测试用例的执行顺序，根据测试方法的名字的先后进行执行

# 8. TestFixture 测试固件
    # 1.setUp：执行用例的前置条件。（在写测试用例的时候，每次操作其实都是基于打开浏览器输入对应网址这些操作）
    # 2.tearDown：执行用例的后置条件。（执行完用例后，为了不影响下一次用例的执行，一般有个数据还原的过程）

    # 3.setupclass：在写测试用例的时候，只执行一次操作其实都是基于打开浏览器输入对应网址这些操作，这个就是执行用例的前置条件。
    # 4.tearDownclass：执行完用例后，关闭浏览器操作，给数据还原，这就是执行用例的后置条件。

 # 区别：setUp,tearDown 每条用例都执行
 #      setUpclass, tearDownclass 整个类中执行一次,且需要用@classmethod装饰


# 9 .测试报告输出：
# 方式一：输出到txt文档

    # with open('测试报告.txt','w+') as file:
    #     unittest.TextTestRunner(stream=file, verbosity=2).run()   #stream:输出地址, verbosity：报告详细程度，2最详细


# 方式二： 输出到html文件，导入第三方html报告模板（HTMLTestRunnerNew.py）,放入到python的安装路径下

    # with open('测试报告.html','wb+') as file:  # wb+:html必须为二进制写入模式
    #     HTMLTestRunnerNew.HTMLTestRunner(stream=file, title='单元测试报告',description='数学计算测试',tester='溪贝').run()





''' 编写用例的写法 '''

# class Sai: # 数学计算类
#
#     def add(self, a, b):  # 加法
#         print('加法计算的结果为：', a+b)
#
#     def sub(self, a, b): # 减法
#         print('减法计算的结果为：', a-b)
#
#
# import unittest
# class TestSai(unittest.TestCase):
#
#     ''' 测试类：测试sai类 '''
#
#     def test_add_positive(self):  # 正数相加用例
#         Sai().add(1, 100)
#
#     def test_add_negative(self):  # 负数相加用例
#         Sai().add(-1, -100)
#
#     def test_add_zero(self):  # 为零相加用例
#         Sai().add(0, 0)
#
#     def test_sub_positive(self):  # 正数相减用例
#         Sai().sub(1, 100)
#
#     def test_sub_negative(self):  # 负数相减用例
#         Sai().sub(-1, -100)
#
#     def test_sub_zero(self):  # 为零相减用例
#         Sai().sub(0, 0)


''' 优化版：用断言assertEqual比对结果'''

class Sai:  # 数学计算类

    def add(self, a, b):  # 加法
        return a+b  # 返回结果

    def sub(self, a, b):  # 减法
        return a-b  # 返回结果


'''测试类'''

import unittest
class TestSai(unittest.TestCase):

    ''' 测试sai类 '''

    @classmethod
    def setUpClass(cls):
        print('即将开始测试数学计算sai的')

    @classmethod
    def tearDownClass(cls):
        print('测试数学计算sai结束')

    def setUp(self): # 重写
        print("****开始进入测试****")

    def tearDown(self):
        print("****测试结束****")

    def test_add_positive(self):  # 正数相加用例
        # print("****开始进入测试****")
        actual = Sai().add(1, 100)  # 实际结果
        # print("****测试结束****")
        print('实际结果为{}'.format(actual))
        expect = 101   # 期望结果
        print("期望结果为{}".format(expect))
        self.assertEqual(actual, expect)  # 对比结果，如果实际值跟期望值相同即通过，反之不通过


    def test_add_negative(self):  # 负数相加用例
        # print("****开始进入测试****")
        actual = Sai().add(-1, -100)  # 实际结果
        # print("****测试结束****")
        print('实际结果为{}'.format(actual))
        expect = -101  # 期望结果
        print("期望结果为{}".format(expect))
        self.assertEqual(actual, expect)

    def test_add_zero(self):  # 为零相加用例
        # print("****开始进入测试****")
        actual = Sai().add(0, 0)  # 实际结果
        # print("****测试结束****")
        print('实际结果为{}'.format(actual))
        expect = 0  # 期望结果
        print("期望结果为{}".format(expect))
        self.assertEqual(actual, expect)

    def test_sub_positive(self):  # 正数相减用例
        # print("****开始进入测试****")
        actual = Sai().sub(1, 100)  # 实际结果
        # print("****测试结束****")
        print('实际结果为{}'.format(actual))
        expect = -99  # 期望结果
        print("期望结果为{}".format(expect))
        self.assertEqual(actual, expect)

    def test_sub_negative(self):  # 负数相减用例
        # print("****开始进入测试****")
        actual = Sai().sub(-1, -100)  # 实际结果
        # print("****测试结束****")
        print('实际结果为{}'.format(actual))
        expect = 99  # 期望结果
        print("期望结果为{}".format(expect))
        self.assertEqual(actual, expect)

    def test_sub_zero(self):  # 为零相减用例
        # print("****开始进入测试****")
        actual = Sai().sub(0, 0)  # 实际结果
        # print("****测试结束****")
        print('实际结果为{}'.format(actual))
        expect = 0   # 期望结果
        print("期望结果为{}".format(expect))
        self.assertEqual(actual, expect)







