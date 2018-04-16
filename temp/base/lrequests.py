#coding=utf-8

import requests
import json
"""
安装
pip install request
pip install --upgrader request 升级
baidu搜索python reqests下载 python setup.py install
查看
在python命令行中
import requests


待学习：json
"""

#POST数据格式是dict
"""
url
data
"""
class RunMail():
    def __init__(self):
        self.res = None

    def send_post(self, url, data):
        res = requests.post(url=url, data=data)
        return res

    def send_get(self, url, data):
        res = requests.get(url=url, data=data)
        return res

    def rum_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)

        self.res = res

        #return self.res

if __name__ == "__main__":

    data = {
        'username': 'annni',
        'password': '111111'
    }
    url = 'http://127.0.0.1:8001/start/'
    run = RunMail()
    run.rum_main(url, "GET", data)
    print(run.res)