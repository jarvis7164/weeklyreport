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
from flask_restful import Resource, Api, marshal
# from flask_restful import reqparse # 用于请求的参数解析
from api.v1.models import app, Role, User, Task, Department, Product
from api.v1.serializers import *

api = Api(app)

"""格式化返回结果"""


def return_true_json(data):
    return jsonify({
        "status": 1,
        "data": data,
        "msg": "request successfully"
    })


def return_false_json(data):
    return jsonify({
        "status": 0,
        "data": data,
        "msg": "request failed"
    })


# 日期格式转换，讲string格式日期转换成datatime格式
def str_to_datatime(time_str):
    time_list = time_str[0:10].split("-")
    year = time_list[0]
    month = time_list[1]
    day = time_list[2]
    return datetime.date(int(year), int(month), int(day))


# 计算预期天数
def get_diviation(planfinished_time, finished_time):
    if finished_time:
        diviation = (str_to_datatime(finished_time) - str_to_datatime(planfinished_time)).days
        return diviation
    else:
        return None


"""定义资源"""


class Hello(Resource):
    def get(self):
        return 'Hello Flask-restful!'


class Login(Resource):
    def post(self):
        args = parser_login.parse_args()
        account = User.query_account(args['account'])
        res = [marshal(account, resource_user_fields)]
        print(type(account))
        password = args['password']
        print(password)
        if account and password == account.password:
            return return_true_json(res)
        else:
            return return_false_json(res)


# 任务列表接口
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
        creat_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print(planfinished_time)
        # print(type(planfinished_time))
        task = Task(task_type=task_type,
                    pdt_id=pdt_id,
                    content=content,
                    planfinished_time=planfinished_time,
                    finished_percent=finished_percent,
                    create_time=creat_time,
                    user_id=user_id,
                    remark=remark)
        task.add_to_db()
        if (task.task_id is None):
            return return_false_json("任务插入失败")
        else:
            return return_true_json("任务新增成功")

    def put(self):
        args = parser_task.parse_args()
        task_id = args['task_id']
        task_type = args['task_type']
        pdt_id = args['pdt_id']
        content = args['content']
        planfinished_time = args['planfinished_time']
        finished_percent = args['finished_percent']
        user_id = args['user_id']
        remark = args['remark']

        task = Task.query_task_id(task_id)
        task.task_type = task_type
        task.pdt_id = pdt_id
        task.content = content
        task.planfinished_time = planfinished_time
        task.finished_percent = finished_percent
        task.user_id = user_id
        task.remark = remark
        Task.commit(self)
        return return_true_json("任务更新成功")

    def get(self):
        datas = Task.find_all()
        print(datas)
        print(type(datas))
        als = []
        #把user_name字段加入到task的返回数据中
        for i in range(len(datas)):
            to_json = {'task_id': datas[i].task_id,
                       'content': datas[i].content,
                       'task_type': datas[i].task_type,
                       'pdt_id': datas[i].pdt_id,
                       'planfinished_time': datas[i].planfinished_time,
                       'finished_time': datas[i].finished_time,
                       'finished_percent': datas[i].finished_percent,
                       'create_time': datas[i].create_time,
                       'user_id': datas[i].user_id,
                       'remark': datas[i].remark,
                       'deviation': get_diviation(datas[i].planfinished_time, datas[i].finished_time),
                       'delete_flag': datas[i].delete_flag,
                       'user_name': Task.query_user_name(datas[i].user_id).user_name
                       }
            als.append(to_json)
        # return als

        res = [marshal(al, resource_task_fields) for al in als]
        if res:
            return return_true_json(res)
        else:
            return return_false_json(res)

    def delete(self):
        args = parser_task.parse_args()
        task_id = args['task_id']
        delete_flag = args['delete_flag']

        task = Task.query_task_id(task_id)
        task.delete_flag = delete_flag
        Task.commit(self)
        return return_true_json("删除成功")


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

        user = User(account=account,
                    password=password,
                    user_name=user_name,
                    create_account=create_account,
                    create_time=create_time,
                    role_id=role_id,
                    dept_id=dept_id,
                    status=status,
                    delete_flag=delete_flag)
        print(user.user_name)
        user.add_to_db()
        if (user.user_id is None):
            return return_false_json("插入失败")
        else:
            return return_true_json("新增成功")

    def get(self):
        datas = User.find_all()
        res = [marshal(data, resource_user_fields) for data in datas]
        if datas:
            return return_true_json(res)
        else:
            return return_false_json(res)

    def put(self):
        args = parser_user.parse_args()
        user_id = args['user_id']
        account = args['account']
        password = args['password']
        user_name = args['user_name']
        role_id = args['role_id']
        dept_id = args['dept_id']
        status = args['status']

        user = User.query_user_id(user_id)
        user.account = account
        user.password = password
        user.user_name = user_name
        user.role_id = role_id
        user.dept_id = dept_id
        user.status = status
        User.commit(self)
        return return_true_json("用户更新成功")

    def delete(self):
        args = parser_user.parse_args()
        user_id = args['user_id']
        delete_flag = args['delete_flag']

        user = User.query_user_id(user_id)
        user.delete_flag = delete_flag
        User.commit(self)
        return return_true_json("用户删除成功")


class RoleList(Resource):
    def get(self):
        datas = Role.find_all()
        res = [marshal(data, resource_role_fields) for data in datas]
        if datas:
            return return_true_json(res)
        else:
            return return_false_json(res)

    def post(self):
        args = parser_role.parse_args()
        role_name = args['role_name']
        role = Role(role_name=role_name)
        role.add_to_db()
        return return_true_json("新增成功")

    def put(self):
        args = parser_role.parse_args()
        role_id = args['role_id']
        role_name = args['role_name']

        role = Role.find_by_id(role_id)
        role.role_name = role_name
        Role.commit(self)
        return return_true_json("角色更新成功")

    def delete(self):
        args = parser_role.parse_args()
        role_id = args['role_id']

        role = Role.find_by_id(role_id)
        Role.delete(role)
        return return_true_json("删除成功")


class DepartmentList(Resource):
    def get(self):
        datas = Department.find_all()
        res = [marshal(data, resource_department_fields) for data in datas]
        if datas:
            return return_true_json(res)
        else:
            return return_false_json(res)

    def post(self):
        args = parser_department.parse_args()
        department_name = args['department_name']
        department = Department(department_name=department_name)
        department.add_to_db()
        return return_true_json("部门新增成功")

    def put(self):
        args = parser_department.parse_args()
        dept_id = args['dept_id']
        department_name = args['department_name']

        department = Department.find_by_id(dept_id)
        department.department_name = department_name
        Department.commit(self)
        return return_true_json("部门更新成功")

    def delete(self):
        args = parser_department.parse_args()
        dept_id = args['dept_id']

        department = Department.find_by_id(dept_id)
        Department.delete(department)
        return return_true_json("部门删除成功")


class ProductList(Resource):
    def get(self):
        datas = Product.find_all()
        res = [marshal(data, resource_product_fields) for data in datas]
        if datas:
            return return_true_json(res)
        else:
            return return_false_json(res)

    def post(self):
        args = parser_product.parse_args()
        product_name = args['product_name']
        product = Product(product_name=product_name)
        product.add_to_db()
        return return_true_json("产品新增成功")

    def put(self):
        args = parser_product.parse_args()
        pdt_id = args['pdt_id']
        product_name = args['product_name']

        product = Product.find_by_id(pdt_id)
        product.product_name = product_name
        Product.commit(self)
        return return_true_json("产品更新成功")

    def delete(self):
        args = parser_product.parse_args()
        pdt_id = args['pdt_id']

        product = Product.find_by_id(pdt_id)
        Product.delete(product)
        return return_true_json("产品删除成功")