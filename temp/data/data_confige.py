#coding=utf-8

"""
类是变量的形式
"""
class global_var:
    #case_id
    id = 0
    url = 2
    isrun = 3
    method = 4
    header = 5
    depend = 6
    depend_key= 7
    depend_value = 8
    request_data = 9
    expect = 10
    result = 11

# 获取caseid
def get_id():
    return global_var.id

def get_url():
    return global_var.url

def get_isrun():
    return global_var.isrun

def get_method():
    return global_var.method

def get_header():
    return global_var.header

def get_depend():
    return global_var.depend

def get_depend_key():
    return global_var.depend_key

def get_depend_value():
    return global_var.depend_value

def get_requestdata():
    return global_var.request_data

def get_expert():
    return global_var.expect

def get_result():
    return global_var.result

def get_header_value():
    header = {
        "header": "1234555"
    }
    return header


