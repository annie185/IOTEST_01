#coding=utf-8
import xlrd
from xlutils.copy import copy as xlcopy

"""
EXCEL操作
思考：
1.不知道路径
2.不知道多少行
3.执行内容
"""


#data = xlrd.open_workbook('../confige/case1.xls')
#tables = data.sheets()[0]
#print(tables.nrows)
#print(tables.cell_value(2,2))

class OperationExcel:
    def __init__(self, file_name = None, sheet_id = None):
        if file_name:
            self.file_name =file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../confige/case1.xls'
            self.sheet_id = 0

        self.data = self.get_data()
    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取一行内容
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获得单元格内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    #写入数据
    def write_value(self, row, col, value):
        """
        写入excel数据
        :param row:
        :param col:
        :param value:
        :return:
        这部份没有弄明白，后续继续加强
        """
        #xlwt:写的之前的文件的数据就不存在了
        read_excl = xlrd.open_workbook(self.file_name)
        write_data = xlcopy(read_excl)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    def get_row_values(self, row):
        """
        根据行号得到整行的数据
        :param row:xlrd
        :return:
        """
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    def get_rowdata_bye_case_vaule(self, case_value):
        """
        通过行号获取整行数
        :param case_value:
        :return:
        """
        row_num = self.get_line_by_case_value(case_value)
        row_data = self.get_row_values(row_num)
        return row_data


    def get_line_by_case_value(self, case_value):
        """
        根所case_value获取对应的行号
        :param case_value:
        :return:
        """
        num = 0
        data = None
        tables = self.data
        row_num = tables.nrows
        cols_data = self.get_cols_data()
        for i in range(1, row_num):
            if case_value == cols_data[i]:
                num = i

        return num


    def get_cols_data(self, col_id=None):
        """
        获取整列数据
        :param col_id:
        :return:
        """
        if col_id !=None:
            cols = self.data.col_values(col_id)
        else:
            #默认取caseid这列的数据的内容
            cols = self.data.col_values(0)

        return cols

    # def get_depend_key(self, row):
    #     """
    #     获取依赖数据的key
    #     :param row:
    #     :return:
    #     """
    #     get_depend_value
    #
    #
    #     pass




if __name__ == "__main__":
    opers = OperationExcel()
    print(opers.get_cell_value(3,4))

