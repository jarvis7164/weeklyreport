#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 19:49
# @Author  : jarvis
# @File    : serializers.py
# @Software: PyCharm
# @Contact : 309194437@.com
from flask_restful import reqparse,fields
"""请求参数解析"""
parser_user = reqparse.RequestParser()
parser_user.add_argument('account', type=str, required=True)
parser_user.add_argument('password', type=str, required=True)
parser_user.add_argument('user_name', type=str, required=True)
parser_user.add_argument('create_account', type=str, required=True)
parser_user.add_argument('create_time', type=str, required=True)
parser_user.add_argument('role_id', type=int, required=True)
parser_user.add_argument('dept_id', type=int, required=True)
parser_user.add_argument('status', type=bool, required=True)
parser_user.add_argument('delete_flag', type=bool, required=True)

parser_login = reqparse.RequestParser()
parser_login.add_argument('account',type=str,required=True)
parser_login.add_argument('password',type=str,required=True)

parser_role = reqparse.RequestParser()
parser_role.add_argument('role_name',type=str,required=True)

parser_department = reqparse.RequestParser()
parser_department.add_argument('department_name',type=str,required=True)

parser_product = reqparse.RequestParser()
parser_product.add_argument('product_name',type=str,required=True)

parser_task = reqparse.RequestParser()
parser_task.add_argument('content', type=str, required=True)
parser_task.add_argument('task_type', type=int, required=True)
parser_task.add_argument('pdt_id', type=int, required=True)
parser_task.add_argument('planfinished_time', type=str, required=True)
# parser_task.add_argument('finished_time', type=str, required=True)
parser_task.add_argument('finished_percent', type=str, required=True)
# parser_addtask.add_argument('create_time', type=str, required=True)
parser_task.add_argument('user_id', type=int, required=True)
parser_task.add_argument('remark', type=str, required=True)



"""序列化返回结果"""
resource_role_fields = {
	'role_id':fields.Integer,
	'role_name':fields.String
}


