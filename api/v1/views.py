#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 19:52
# @Author  : jarvis
# @File    : views.py
# @Software: PyCharm
# @Contact : 309194437@qq.com
"""接口实现"""
import datetime

from flask import jsonify
from flask_restful import Resource,Api,marshal
# from flask_restful import reqparse # 用于请求的参数解析
from api.v1.models import app,Role,User,Task
from api.v1.serializers import *
api = Api(app)

"""格式化返回结果"""
def return_true_json(data):
	return jsonify({
		"status":1,
		"data":data,
		"msg":"request successfully"
	})
def return_false_json(data):
	return jsonify({
		"status":0,
		"data":data,
		"msg":"request failed"
	})

"""定义资源"""
class Hello(Resource):
	def get(self):
		return 'Hello Flask-restful!'

#用户登录接口
class Login(Resource):
	# def get(self):
	# 	return "登录成功"
	def post(self):
		args = parser_login.parse_args()
		account =User.query_account(args['account'])
		print(type(account))
		password = args['password']
		print(password)
		if account and password==account.password:
			return '{"msg":"登录成功"}'
		else:
			return '{"msg":"账号密码错误"}'

#新增任务接口
class Tasklist(Resource):
	def post(self):
		args = parser_task.parse_args()
		task_type = args['task_type']
		pdt_id = args['pdt_id']
		content = args['content']
		planfinished_time = args['planfinished_time']
		finished_percent = args['finished_percent']
		user_id = args['user_id']
		remark = args['remark']
		data = Task(task_type=task_type,
					pdt_id=pdt_id,
					content=content,
					planfinished_time=planfinished_time,
					finished_time="null",
					finished_percent=finished_percent,
					create_time= datetime.datetime.now(),
					user_id=user_id,
					remark=remark)
		Task.add_to_db(data)
		return  "新增成功"

class UserList(Resource):
	def post(self):
		args = parser_user.parse_args()
		account = args['account']
		password = args['password']
		user_name = args['user_name']
		create_account = args['create_account']
		create_time = args['create_time']
		role_id = args['role_id']
		dept_id = args['dept_id']
		status = args['status']
		delete_flag = args['delete_flag']
		
		user = User(account = account,
		password = password,
		user_name = user_name,
		create_account = create_account,
		create_time = create_time,
		role_id = role_id,
		dept_id = dept_id,
		status = status,
		delete_flag = delete_flag)
		print(user.user_name)
		user.add_to_db()
		if (user.user_id is None):
			return False
		else:
			return True
	def get(self):
		return '1'
	
class RoleList(Resource):
	def get(self):
		datas = Role.find_all()
		res = [marshal(data,resource_role_fields) for data in datas]
		if datas:
			return return_true_json(res)
		else:
			return return_false_json(res)
	
	def post(self):
		args = parser_role.parse_args()
		role_name = args['role_name']
		role = Role(role_name=role_name)
		role.add_to_db()
		
class DepartmentList(Resource):
	pass

class ProductList(Resource):
	pass
