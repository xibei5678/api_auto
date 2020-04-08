#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : context.py
@Date  : 2020/4/8 0008 16:17
@Author: xibei
'''


class Context:

    normal_name = "13201231231"
    pwd = "123456"



# class DoRegex:

    # @staticmethod
    # def replace(data, replace,):
    #     pattern = '\$\{(.*?)\}'
    #     import re
    #     if re.search(data,pattern):
    #




if __name__ == '__main__':

    import re

    data = '{"mobilephone":"${normal_name}", "pwd":"${pwd}"}'
    pa = '\$\{(.*?)\}'
    while re.search(pattern=pa, string=data):
        a = re.search(pattern=pa, string=data)
        print(a.group(1))
        value = getattr(Context, a.group(1))
        data = re.sub(pa, value, data, count=1)  # count:一次替换一个，默认0为全部替换

    print(data)