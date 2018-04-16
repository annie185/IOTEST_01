#coding=utf-8

import json
"""
python的编码方式
"""
class CommonUtil:
    def is_contain(self, str_one, str_two):
        """

        :param str_one: 查找的字符串
        :param str_two: 被查找的字符串
        :return:
        """
        flag = False
        #if isinstance(str_one, unicode):
        #str_one = str_one.encode('unicode-escape').decode('string_escape')

        if str_one in str_two:
            flag = True

        return flag

if __name__ == "__main__":
    cctest1 = '"user": "aqf"'
    cctest2 = '{"user": "aqf", "pw": "123456"}'

    print(type(cctest1))
    rt = CommonUtil()

    print(rt.is_contain(cctest1, cctest2))
