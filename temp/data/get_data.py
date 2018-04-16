#coding=utf-8

from uitl.operation_excel import  OperationExcel
from data.data_confige import *
from uitl.operation_json import OperationJson

class GetData:
    def __init__(self):
        self.oper_excel = OperationExcel()

    def get_case_lines(self):
        return self.oper_excel.get_lines()

    def get_is_run(self, row):
        flag =None
        col = get_isrun()
        run_modle = self.oper_excel.get_cell_value(row, col)
        if run_modle == 'yes':
            flag = True
        else:
            flag = False

        return flag

    def get_is_header(self, row):
        col = get_header()
        header_modle = self.oper_excel.get_cell_value(row, col)
        if header_modle == 'yes':
            return get_header_value()
        else:
            return None

    def get_method(self, row):
        col = get_method()
        method_modle = self.oper_excel.get_cell_value(row, col)
        return method_modle

    def get_url(self, row):
        col = get_url()
        url = self.oper_excel.get_cell_value(row, col)
        return url

    def is_depend(self, row):

        col = get_depend()
        depend = self.oper_excel.get_cell_value(row, col)
        if depend == '':
            return None
        else:
            return depend

    def get_depend_value(self, row):
        col = get_depend_key()
        depend_value = self.oper_excel.get_cell_value(row, col)
        return depend_value

    def get_depend_key(self, row):
        col = get_depend_key()
        depend_key = self.oper_excel.get_cell_value(col, row)
        return depend_key

    def get_request_data(self, row):
        col = get_requestdata()
        data = self.oper_excel.get_cell_value(row, col)
        if data == '':
            return None
        return self.get_data_for_json(data)

    def get_data_for_json(self, id):
        oper_json = OperationJson()
        return oper_json.get_data(id)

    def get_except_data(self, row):
        col = get_expert()
        except_data = self.oper_excel.get_cell_value(row, col)
        if except_data == '':
            return None
        return except_data

    def get_result_value(self, row, value):
        col = get_result()
        self.oper_excel.write_value(row, col, value)




if __name__ =="__main__":
    get_test_data = GetData()
    print(get_test_data.get_request_data(1))
