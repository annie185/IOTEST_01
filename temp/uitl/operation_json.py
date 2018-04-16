#coding=utf-8

import json


#fp = open("../confige/login.json")
#加载json文件
#data = json.load(fp)
#print(data)

class OperationJson:
    def __init__(self):
        self.data = self.read_data()

    #读取json
    def read_data(self):
        with open("../confige/login.json") as fp:
            # 加载json文件
            data = json.load(fp)
            return data

    def get_data(self, id):
        return self.data[id]

if __name__ == "__main__":
    opjson = OperationJson()
    print(opjson.get_data("login"))