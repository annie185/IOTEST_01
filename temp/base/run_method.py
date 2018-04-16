#coding=utf-8

import  requests
import json

class RunMethod:
    def post_main(self, url, data, header = None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res

    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        return res

    def run_main(self, method, url, data=None, header=None):
        res =None
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        #todo：此处可以返回数据和状态码，在后面判断的时候，可以进行相关的判断
        #return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        #print(res.status_code)
        #print(res.text)
        return json.dumps(res.json())