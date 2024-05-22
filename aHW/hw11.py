"""
接口请求任务，用python实现接口调用，贴出调用成功的结果图
任务：
1) 接口请求任务，用python实现接口调用，贴出调用成功的结果图
    背景：https://note.wps.cn/
    访问wps便签，登录新建一条便签数据后，
    抓包
请求头必填项：wps_sid、content-type
"""
import requests
url="https://note.wps.cn/"

url="https://account.wps.cn/api/v3/mine?attrs=profile"
method="get"