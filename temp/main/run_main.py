#coding=utf-8

from base.run_method import RunMethod
from data.get_data import GetData
from uitl.common_util import CommonUtil
from data.dependent_data import DependentData
import json
"""
练习python内置函数用法
import sys
sys.path.append("")
"""
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.depend = None

    def go_on_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            url = self.data.get_url(i)
            method = self.data.get_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_request_data(i)
            exceptdata = self.data.get_except_data(i)
            header = self.data.get_is_header(i)

            depend_case = self.data.is_depend(i)
            if depend_case:
                self.depend = DependentData(depend_case)
                # depend的响应数据
                depend_data = self.depend.get_data_for_key(i)
                depend_key = self.data.get_depend_key(i)
                data[depend_key] = depend_data

            if is_run:
                res = self.run_method.run_main(method, url, data, header)

            result = CommonUtil()
            if result.is_contain(exceptdata, res):
                self.data.get_result_value(i, 'pass')
                print("测试通过")
            else:
                self.data.get_result_value(i, 'fail')
                print("测试不通过")


if __name__ == "__main__":
    run = RunTest()
    run.go_on_run()