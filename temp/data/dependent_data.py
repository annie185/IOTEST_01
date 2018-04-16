#coding=utf-8
from uitl.operation_excel import OperationExcel
from base.run_method import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse

class DependentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_depeddata = OperationExcel()
        self.data = GetData()

    def get_case_line_data(self):
        """
        根据case_id的值获取case的整行的内容
        :return:
        """
        row_data = self.opera_depeddata.get_rowdata_bye_case_vaule(self.case_id)
        return row_data

    def run_dependent(self):
        """
        运行依赖测试用例
        :return:
        """
        res = None
        run_method = RunMethod()
        row_num = self.opera_depeddata.get_line_by_case_value(self.case_id)
        request_data = self.data.get_request_data(row_num)
        header = self.data.get_is_header(row_num)
        url = self.data.get_url(row_num)
        method = self.data.get_method(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return res

    def get_data_for_key(self, row):
        """
        根据依赖数据的key去执行依赖测试case的响应，然后返回
        :param row:
        :return:
        """
        depend_data = self.data.get_depend_value(row)
        response_data = self.run_dependent()
        #jsonpath
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        # python高级函数
        return [math.value for math in madle]


