#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : context.py
@Date  : 2020/4/8 0008 16:17
@Author: xibei
'''


class Context:

    normal_name = "13201231230"
    pwd = "123456"




class DoRegex:

    @staticmethod
    def replace(str_data, replace_value=None):  # 如果单个匹配，直接输入匹配值，进行匹配，多个匹配值时，通过Context进行取值匹配
        pattern = '\$\{(.*?)\}'
        import re
        from python_api_test_qianchendai.common.read_conf import DoConf
        if replace_value:
            str_data = re.sub(pattern, replace_value, str_data, count=1)
        else:
            while re.search(pattern=pattern, string=str_data):
                a = re.search(pattern=pattern, string=str_data)
                if hasattr(Context, a.group(1)):  # 如果Context中没有，从配置文件中获取 。a.group(1)获取分组1的匹配值
                    value = getattr(Context, a.group(1))
                    str_data = re.sub(pattern, value, str_data, count=1)
                else:
                    try:
                        setattr(Context, a.group(1), DoConf().get_conf_str("regex", a.group(1)))  # 从配置文件中获取值并新增到Context中
                    except BaseException as e:
                        raise e
                    value = getattr(Context, a.group(1))
                    str_data = re.sub(pattern, value, str_data, count=1)

        return str_data



if __name__ == '__main__':

    import re

    # data_1 = '{"mobilephone":"${normal_name}", "pwd":"${pwd}"}'
    # data_2 = '{"mobilephone": "${normal_name}", "pwd": 12345678}'
    pa = '\$\{(.*?)\}'
    # while re.search(pattern=pa, string=data):
    #     a = re.search(pattern=pa, string=data)
    #     print(a.group(1))
    #     value = getattr(Context, a.group(1))
    #     data = re.sub(pa, value, data, count=1)  # count:一次替换一个，默认0为全部替换
    # c = re.sub(pa,'13201231230',data_2)
    # print(c)
    #
    # print(data)
    # b = DoRegex.replace(data_2)
    # print(b)
    # c = DoRegex.replace(data_2, '1320123120')
    # print(c)

    pat = '^[1](([3][0-9])|([4][5-9])|([5][0-3,5-9])|([6][5,6])|([7][0-8])|([8][0-9])|([9][1,8,9]))[0-9]{8}$'
    str_1 = '19000000000'
    # a = re.search(pattern=pat, string=str_1)
    # print(a)
    # print(str_1)
    while re.search(pattern=pat, string=str_1) is None:
        print(str_1)
        print("phone:{}不符合手机号码格式".format(str_1))
        str_1 = str(int(str_1)+100000000)
        # a = re.search(pattern=pat, string=str_1)

    print(str_1)