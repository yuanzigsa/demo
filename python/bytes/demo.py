# @Author  : yuanzi
# @Time    : 2024/10/2 14:54
# Website: https://www.yzgsa.com
# Copyright (c) <yuanzigsa@gmail.com>

import hashlib

string = "123456"

m = hashlib.md5()       # 创建md5对象
str_bytes = string.encode(encoding='utf-8')
print(type(str_bytes))
m.update(str_bytes)   # update方法只接收bytes类型数据作为参数
str_md5 = m.hexdigest()     # 得到散列后的字符串

print('MD5散列前为 ：' + string)
print('MD5散列后为 ：' + str_md5)