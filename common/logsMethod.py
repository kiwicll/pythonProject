import inspect
import os
from datetime import datetime
from colorama import Fore
from main import DIR
import functools

"""日志输出格式方法"""
def info(text):
    stack = inspect.stack()
    fromatted_time=datetime.now().strftime('%H:%M:%S:%f')[:-3]#定义了日志的输出时间
    cede_path=f"{os.path.basename(stack[1].filename)}:{stack[1].lineno}"#当前执行文件的绝对路径和
    content=f"[INFO]{fromatted_time}-{cede_path}>>{text}"
    print(Fore.LIGHTGREEN_EX+content)
    str_tinme=datetime.now().strftime("%Y%m%d")
    with open(file=DIR+'\\logs\\'+f'{str_tinme}_info.log',mode='a',encoding='utf-8') as f:
        f.write(content+'\n')

""" 日志装饰器   """
def case_log_init(func):
    @functools.wraps(func)#解决参数冲突问题
    def inner(*args,**kwargs):
        class_name=args[0].__class__.__name__ #获取类名
        method_name=func.__name__ #获取方法名
        docstring=inspect.getdoc(func)#获取方法注释
        print(Fore.LIGHTRED_EX+'----------------------------')
        info(f"Class name:{class_name}")
        info(f"Method name:{method_name}")
        info(f"Test Description:{docstring}")
        func(*args,**kwargs)
    return inner()

"""类级别装饰器"""
def class_case_log(cls):
    """ 用例的日志装饰器级别 """
    for name,method in inspect.getmembers(cls,inspect.isfunction()):
        if name.startswith('testCase'):
            setattr(cls,name,case_log_init())
    return cls