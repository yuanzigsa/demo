# @Author  : yuanzi
# @Time    : 2024/10/2 14:20
# Website: https://www.yzgsa.com
# Copyright (c) <yuanzigsa@gmail.com>

import threading

# 全局变量
counter = 0


def increment_counter():
    global counter
    for _ in range(100000):
        counter += 1


# 创建多个线程
threads = []
for i in range(100):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

# 期望的结果是 1000000 (10 * 100000)
print(f"程序1最终的 counter 值: {counter}")


# 全局变量
counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

# 创建多个线程
threads = []
for i in range(100):
    t = threading.Thread(target=increment_counter)
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

# 正确的 counter 值
print(f"程序2最终的 counter 值: {counter}")