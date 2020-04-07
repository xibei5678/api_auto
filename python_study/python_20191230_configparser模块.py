#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : python_20191230_configparser模块.py
@Date  : 2019/12/30 0030 10:55
@Author: xibei
'''


'''配置文件'''

# 1. 实现用户可配置
# 2. 一般以.ini .conf .properties 等等为后缀的文件
# 3. 一般包含section（片段）、option（选项）
# 内容书写格式：（参见“python_20191230_配置文件”）
# [section_1]
#  option_1=值
#  option_2=值
# [section_2]
#  option_1=值
#  option_2=值
#

# 4. 读取出来的数据类型都是字符串
# 5. 配置文件中“# 或 ；”符号进行注释


'''configparser 模块'''

# 1. 用于配置文件的读取
# 2. 第三方模块，需安装：pip install configparser

import configparser

# 创建对象
cf = configparser.ConfigParser()

# 打开待读取文件
# cf.read('python_20191230_配置文件.conf', encoding='utf-8')  # 配置文件中如果有中文，需设置编码

# 获取所有的section片段
# print(cf.sections())  # 返回list

# 获取某片段下所有option
# print(cf.options('students'))  # 返回list

# 获取指定的option值
# print(cf.get('students', 'name'))  # 优先使用该方法
# print(cf['students']['name'])

# 向配置文件中添加section
# cf.add_section("user")

# 添加option 和值
# cf.set(section="user", option="name", value="啦啦")

# 像配置文件中写入或修改都需要此操作 否则文件未被修改
# with open("python_20191230_配置文件.conf", "a+", encoding="utf-8") as f:
#     cf.write(f)


if __name__ == '__main__':

    cf = configparser.ConfigParser()
    cf.read('python_20191230_配置文件.conf', encoding='utf-8')
    sect = "user"
    if sect not in cf.sections():
        cf.add_section(sect)
        cf.set(section=sect, option="phone", value="123456")
        with open("python_20191230_配置文件.conf", "w+", encoding="utf-8") as f:
            cf.write(f)
    else:
        cf.set(section=sect, option="phone", value="123456")
        with open("python_20191230_配置文件.conf", "w+", encoding="utf-8") as f:
            cf.write(f)

