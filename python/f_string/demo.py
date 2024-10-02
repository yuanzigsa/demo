# @Author  : yuanzi
# @Time    : 2024/10/2 15:18
# Website: https://www.yzgsa.com
# Copyright (c) <yuanzigsa@gmail.com>

from datetime import datetime

# 时间格式化
now = datetime.now()
print(now.strftime("%Y-%m-%d"))     # 2022-04-22
print(f"{now:%Y-%m-%d}")            # 2022-04-22

# 设置对齐
word = "hello"
print(f"{word:*^10}")   # 居中对齐
print(f"{word:*>10}")   # 右对齐
print(f"{word:*<10}")   # 左对齐


# 格式化类对象
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"User's name is: {self.first_name} {self.last_name}"

user = User("小", "明")

print(f"{user}")
print(f"{user!r}")