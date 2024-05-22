"""
编写一个名为timer的 Python 装饰器，用于测量函数运行的时间。要求：
使用time模块的time.perf_counter()函数来获取精确的时间。
在函数执行前后分别记录时间，计算函数执行所需的时间。
在函数执行后打印出函数名称及其执行时间（单位：秒）。
# 你的代码
"""
import time
# def timer(func):
#     def F(*args):
#         T1=time.time()
#         A = func(*args)
#         T2=time.time()
#         print(T1)
#         print(T2 )
#         return  A
#     return F
# @timer
# def F1():
#     time.sleep(1)
# F1()

import time


def AA(arg1, arg2):
    def BB(func):
        def CC(*args, **kwargs):
            print(f" {arg1}, {arg2}")
            return func(*args, **kwargs)
        return CC
    return BB
# 使用装饰器，并传递参数
@AA("Hello", "World")
def say_hello():
    print("Hello CN!")
# 调用函数
say_hello()