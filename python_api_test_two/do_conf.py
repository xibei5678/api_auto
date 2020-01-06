#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@File  : do_conf.py
@Date  : 2020/1/6 0006 15:05
@Author: xibei
'''

from configparser import ConfigParser

class DoConf(ConfigParser):

    def __init__(self, conf_file_name):
        super(DoConf, self).__init__()
        self.file_name = conf_file_name


    def __call__(self,section, option=None, is_eval=False, is_bool=False, is_int=False, is_float=False):
        self.read(self.file_name, encoding='utf-8')
        if option is None:
            return dict(self[section])

        if isinstance(is_bool, bool):
            if is_bool:
                return self.getboolean(section, option)
        else:
            return ValueError('is_bool不是bool类型')  # 手动抛出异常

        if isinstance(is_int, bool):
            if is_int:
                return self.getint(section, option)
        else:
            return ValueError('is_int不是bool类型')  # 手动抛出异常

        if isinstance(is_float, bool):
            if is_float:
                return self.getfloat(section, option)
        else:
            return ValueError('is_float不是bool类型')  # 手动抛出异常

        data = self.get(section, option)

        if isinstance(is_eval, bool):
            if is_eval:
                return eval(data)
            else:
                return data
        else:
            return ValueError('is_float不是bool类型')  # 手动抛出异常










if __name__ == '__main__':

    read_conf = DoConf('test_environment.conf')
    print(read_conf('log', 'console_level'))