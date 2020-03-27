

'''json 模块'''


# 1.用于字符串和字典直接的转换
# 2. 为啥不用eval函数：eval函数不能将null转换成None



import json


# 1. 序列化--将dict序列化成str或者file

dict_1 = {'status': 0, 'code': 1001, 'data': None, 'msg': '登录失败'}

# dumps（）：将python格式字典转换成json格式的字符串

# json_str = json.dumps(dict_1, ensure_ascii=False, indent=4)  # ensure_ascii:是否使用ascii编码，indent：缩进
# print(json_str)
# print(type(json_str))

# dump（）：将python格式的字典写入到json格式的文件中

# with open('data.json', 'w') as f:  # 将dict_1 写入到data.json 文件中
#     json.dump(dict_1, f, ensure_ascii=False)


# 2. 反序列化--将str或file反序列化成dict

str_1 = '{"status": 0, "code": 1001, "data": null, "msg": "登录失败"}'

# loads（）：将json的str转换成python的字典

# python_dict = json.loads(str_1)
# print(python_dict)
# print(type(python_dict))


# load（）：将json文件中的str转换成python的字典

# f = open('data.json', 'r')
# file_dict = json.load(f)
# print(file_dict)
# print(type(file_dict))


# str_01 = "{'code':1001,'msg':'手机号错误'}"
# print(type(json.loads(str_01)))


# 注意：str需要是'{"key":}'的格式,key必须为双引号不能为单引号
#      str中如何含有元组（tupe）也会报错，因为字典中的元组和list都对应的json中的数组