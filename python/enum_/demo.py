# @Author  : yuanzi
# @Time    : 2024/10/2 14:32
# Website: https://www.yzgsa.com
# Copyright (c) <yuanzigsa@gmail.com>

import enum


class isp_code(enum.Enum):
    ChinaMobile = 1
    ChinaUnicom = 2
    ChinaTelecom = 3


def get_isp_type(code):
    if code == isp_code.ChinaMobile.value:
        return "移动"
    elif code == isp_code.ChinaUnicom.value:
        return "联通"
    elif code == isp_code.ChinaTelecom.value:
        return "电信"
    else:
        return "未知"


print(get_isp_type(3))


# 枚举值遍历

for item in isp_code:
    print(item.name, item.value)
