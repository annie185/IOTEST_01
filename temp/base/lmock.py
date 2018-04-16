#coding=utf-8

import unittest.mock

#模拟MOCK封装
def mock_test(mock_method, request_data, url, method, response_data):
    mock_method = unittest.mock.Mock(return_value=request_data)
    res = mock_method(url, method, request_data)
    return res


if __name__== "__main__":
    pass