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
parser_user.add_argument('user_id', type=int)
parser_user.add_argument('account', type=str)
parser_user.add_argument('password', type=str)
parser_user.add_argument('user_name', type=str)
parser_user.add_argument('create_account', type=str)
parser_user.add_argument('create_time', type=str)
parser_user.add_argument('role_id', type=int)
parser_user.add_argument('dept_id', type=int)
parser_user.add_argument('status', type=bool)
parser_user.add_argument('delete_flag', type=bool)

parser_login = reqparse.RequestParser()
parser_login.add_argument('account',type=str,required=True)
parser_login.add_argument('password',type=str,required=True)

parser_role = reqparse.RequestParser()
parser_role.add_argument('role_name',type=str)
parser_role.add_argument('role_id',type=int)

parser_department = reqparse.RequestParser()
parser_department.add_argument('dept_id',type=int)
parser_department.add_argument('department_name',type=str)

parser_product = reqparse.RequestParser()
parser_product.add_argument('pdt_id',type=int)
parser_product.add_argument('product_name',type=str)

parser_task = reqparse.RequestParser()
parser_task.add_argument('task_id', type=int)
parser_task.add_argument('content', type=str)
parser_task.add_argument('task_type', type=int)
parser_task.add_argument('pdt_id', type=int)
parser_task.add_argument('planfinished_time', type=str)
# parser_task.add_argument('finished_time', type=str, required=True)
parser_task.add_argument('finished_percent', type=str)
# parser_addtask.add_argument('create_time', type=str)
parser_task.add_argument('user_id', type=int)
parser_task.add_argument('user_name', type=str)
parser_task.add_argument('remark', type=str)
parser_task.add_argument('delete_flag', type=int)



"""序列化返回结果"""
resource_role_fields = {
	'role_id':fields.Integer,
	'role_name':fields.String
}

resource_product_fields = {
	'product_id':fields.Integer,
	'product_name':fields.String
}

resource_department_fields = {
	'dept_id':fields.Integer,
	'department_name':fields.String
}

resource_task_fields = {
	'task_id':fields.Integer,
	'content':fields.String,
	'task_type':fields.Integer,
	'pdt_id':fields.Integer,
	'planfinished_time':fields.String,
	'finished_time':fields.String,
	'finished_percent':fields.String,
	'create_time':fields.String,
	'user_id':fields.Integer,
	'remark':fields.String,
	'delete_flag':fields.String,
	'user_name':fields.String,
    'deviation':fields.String
}

resource_user_fields = {
	'user_id':fields.Integer,
	'account':fields.String,
	'password':fields.String,
	'user_name':fields.String,
	'create_account':fields.String,
	'create_time':fields.String,
	'role_id':fields.Integer,
	'dept_id':fields.Integer,
	'status':fields.Integer,
	'delete_flag':fields.Integer
}

resource_dictitem_fields = {
	'id':fields.Integer,
	'dict_code':fields.String,
	'dict_name':fields.String,
	'keyvalue':fields.String,
}
