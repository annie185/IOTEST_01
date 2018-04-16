#coding=utf-8

import unittest
from base.lrequests import RunMail
import unittest.mock
from base.lmock import mock_test
import json
"""
创建每个类要继承unittest类
类方法只执行一次


作业：了解类方法
"""

class TestMethod(unittest.TestCase):
    """"@classmethod
    def setUpClass(cls):
        print("begin")

    @classmethod
    def tearDownClass(cls):
        print("after")

    #每次方法之前执行
    def setUp(self):
        print('test-->setup')
    #每次方法之后执行
    def tearDown(self):
        print('test-->teardown')"""

    def setUp(self):
        self.run = RunMail()

    """
    所有的case以test开头
    """
    def test_01(self):
        url = 'http://127.0.0.1:8001/start/'
        data = {
            'username': 'annni',
            'password': '111111',
            'errorcode': 1001
        }
        #mock_data = unittest.mock.Mock(return_value=data)
        res = mock_test(self.run.rum_main, data, url, 'POST', data)
        #self.run.rum_main = mock_data
        #res = self.run.rum_main(url, 'POST', data)
        print(res)
        self.assertEqual(res['errorcode'], 1001, "测试失败")


    def test_02(self):
        data = {
            'username': 'annni',
            'password': '111111'
        }
        url = 'http://127.0.0.1:8001/start/'
        self.run.rum_main(url, 'GET', data)
        print(self.run.res)



if __name__ == "__main__":
    unittest.main()