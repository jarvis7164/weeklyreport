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
parser_user.add_argument('pre_condition', type=str,action='append')
parser_user.add_argument('delete_flag', type=bool)
parser_user.add_argument('pre_con_name', type=str)


parser_login = reqparse.RequestParser()
parser_login.add_argument('account',type=str,required=True)
parser_login.add_argument('password',type=str,required=True)

parser_role = reqparse.RequestParser()
parser_role.add_argument('page',type=int)
parser_role.add_argument('per_page',type=int)
parser_role.add_argument('role_name',type=str)
parser_role.add_argument('role_id',type=int)

parser_department = reqparse.RequestParser()
parser_department.add_argument('dept_id',type=int)
parser_department.add_argument('department_name',type=str)

parser_product = reqparse.RequestParser()
parser_product.add_argument('pdt_id',type=int)
parser_product.add_argument('product_name',type=str)

parser_task = reqparse.RequestParser()
parser_task.add_argument('page',type=int)
parser_task.add_argument('per_page',type=int)
parser_task.add_argument('task_id', type=int)
parser_task.add_argument('content', type=str)
parser_task.add_argument('task_type', type=int,action='append')
parser_task.add_argument('task_nature', type=int,default=1)
parser_task.add_argument('pdt_id', type=int,action='append')
parser_task.add_argument('planfinished_time', type=str)
parser_task.add_argument('planstart_time', type=str)
parser_task.add_argument('planstart_time1', type=str)
parser_task.add_argument('planstart_time2', type=str)
parser_task.add_argument('start_time', type=str)
# parser_task.add_argument('finished_time', type=str, required=True)
parser_task.add_argument('finished_percent', type=str)
# parser_addtask.add_argument('create_time', type=str)
parser_task.add_argument('user_id', type=int)
parser_task.add_argument('user_name', type=str,action='append')
parser_task.add_argument('remark', type=str)
parser_task.add_argument('delete_flag', type=int)
parser_task.add_argument('startDate', type=str)
parser_task.add_argument('endDate', type=str)


parser_dictitem = reqparse.RequestParser()
parser_dictitem.add_argument('id',type=int)
parser_dictitem.add_argument('dict_code',type=str)
parser_dictitem.add_argument('dict_name',type=str)
parser_dictitem.add_argument('key_value',type=str,action='append')
# parser_dictitem.add_argument('key_value',type=str)

parser_weeklyreport_output = reqparse.RequestParser()
# parser_weeklyreport_output.add_argument('path',type=str,required=True)
# parser_weeklyreport_output.add_argument('sheet_name',type=str,required=True)
parser_weeklyreport_output.add_argument('data',type=str,required=True,action='append')
# parser_weeklyreport_output.add_argument('value',type=str,required=True,action='append')

parser_weeklyreport_download = reqparse.RequestParser()
parser_weeklyreport_download .add_argument('path',type=str,required=True)

parser_preconditon = reqparse.RequestParser()
parser_preconditon.add_argument('pre_id', type=int)
parser_preconditon.add_argument('user_id', type=int)
parser_preconditon.add_argument('pre_name', type=str)
parser_preconditon.add_argument('pre_condition', type=str)
parser_preconditon.add_argument('page',type=int)
parser_preconditon.add_argument('per_page',type=int)



"""序列化返回结果"""
resource_role_fields = {
	'role_id':fields.Integer,
	'role_name':fields.String
}

resource_product_fields = {
	'pdt_id':fields.Integer,
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
	'task_nature':fields.Integer,
	'task_nature_name':fields.String,
	'task_type_name':fields.String,
	'pdt_id':fields.Integer,
	'product_name':fields.String,
	'planstart_time':fields.String,
	'start_time':fields.String,
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
	# 'password':fields.String,
	'user_name':fields.String,
	'create_account':fields.String,
	'create_time':fields.String,
	'role_id':fields.Integer,
	'dept_id':fields.Integer,
	'pre_condition':fields.String,
	'status':fields.Integer,
	# 'delete_flag':fields.Integer
}

resource_dictitem_fields = {
	'id':fields.Integer,
	'dict_code':fields.String,
	'dict_name':fields.String,
	'key_value':fields.String,
}

resource_precondition_fields = {
	'pre_id':fields.Integer,
	'user_id':fields.Integer,
	'pre_name':fields.String,
	# 'pre_condition':fields.String,
}