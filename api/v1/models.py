#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 19:47
# @Author  : Jarvis
# @File    : models.py
# @Software: PyCharm
# @Contact : 309194437@qq.com
"""数据库模型 ORM"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_

app = Flask(__name__, static_folder='static', static_url_path='/static')  # 定义静态文件的名字和目录
CORS(app, supports_credentials=True)  # 处理跨域问题
app.config.from_pyfile('config.py')  # 加载数据库配置
db = SQLAlchemy(app)


class User(db.Model):
    # 对应的实际表名 wr_user
    __tablename__ = 'wr_user'
    user_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    account = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    user_name = db.Column(db.String(20))
    create_account = db.Column(db.String(20))
    create_time = db.Column(db.String(20))
    role_id = db.Column(db.Integer)
    dept_id = db.Column(db.Integer)
    status = db.Column(db.SmallInteger, default=0)
    delete_flag = db.Column(db.SmallInteger, default=0)

    def __init__(self, account, user_name, password, create_account, create_time, role_id, dept_id, status,
                 delete_flag):
        # self.user_id = user_id
        self.account = account
        self.password = password
        self.user_name = user_name
        self.create_account = create_account
        self.create_time = create_time
        self.role_id = role_id
        self.dept_id = dept_id
        self.status = status
        self.delete_flag = delete_flag

    def add_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()

    def query_account(self):
        return User.query.filter(User.account == self).first()

    def query_user_id(self):
        return User.query.filter(User.user_id == self).first()

    @classmethod
    def find_all(cls):
        return cls.query.filter(User.delete_flag == 0).all()

    def commit(self):
        db.session.commit()


class Role(db.Model):
    __tablename__ = 'wr_role'
    role_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    role_name = db.Column(db.String(20))

    def __init__(self, role_name):
        self.role_name = role_name

    def add_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()

    @classmethod
    def find_by_role_name(cls, role_name):
        return cls.query.filter_by(role_name=role_name).first()

    @classmethod
    def find_by_id(cls, role_id):
        return cls.query.get(role_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.filter().all()

    def commit(self):
        db.session.commit()


class Department(db.Model):
    __tablename__ = 'wr_department'
    dept_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    department_name = db.Column(db.String(20))

    def __init(self, department_name):
        self.department_name = department_name

    def add_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()

    @classmethod
    def find_all(cls):
        return cls.query.filter().all()

    @classmethod
    def find_by_id(cls, dept_id):
        return cls.query.get(dept_id)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def commit(self):
        db.session.commit()


class Product(db.Model):
    __tablename__ = 'wr_product'
    pdt_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    product_name = db.Column(db.String(20))

    def __init(self, product_name):
        self.product_name = product_name

    @classmethod
    def find_all(cls):
        return cls.query.filter().all()

    @classmethod
    def find_by_id(cls, pdt_id):
        return cls.query.get(pdt_id)

    def add_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def commit(self):
        db.session.commit()


class Task(db.Model):
    __tablename__ = 'wr_task'
    task_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    content = db.Column(db.String(1024))
    task_type = db.Column(db.SmallInteger, default=0)
    pdt_id = db.Column(db.Integer)
    # planfinished_time = db.Column(db.DateTime)
    planfinished_time = db.Column(db.String(20))
    # finished_time = db.Column(db.DateTime)
    finished_time = db.Column(db.String(20))
    finished_percent = db.Column(db.String(10))
    # create_time = db.Column(db.DateTime)
    create_time = db.Column(db.String(20))
    user_id = db.Column(db.Integer)
    remark = db.Column(db.String(1024))
    deviation = db.Column(db.String(10))
    delete_flag = db.Column(db.SmallInteger, default=0)

    def __init__(self, content, task_type, pdt_id, planfinished_time, finished_percent,
                 create_time, user_id, remark):

        self.content = content
        self.task_type = task_type
        self.pdt_id = pdt_id
        self.planfinished_time = planfinished_time
        # self.finished_time = finished_time
        self.finished_percent = finished_percent
        self.create_time = create_time
        self.user_id = user_id
        self.remark = remark

    def query_task_id(self):
        return Task.query.filter(Task.task_id == self).first()

    def query_user_name(user_id):
        return User.query.filter(and_(User.delete_flag == 0, User.user_id == user_id)).first()

    @classmethod
    def find_all(cls):
        return cls.query.filter(Task.delete_flag == 0).all()

    def add_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()

    def commit(self):
        db.session.commit()

#数据字典表
class Dictitem(db.Model):
    __tablename__ = 'wr_dictitem'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    dict_code = db.Column(db.String(20))
    dict_name = db.Column(db.String(64))
    key_value = db.Column(db.String(1024))

    def __init__(self, dict_code,dict_name,key_value):
        self.dict_code = dict_code
        self.dict_name = dict_name
        self.key_value = key_value

    @classmethod
    def find_all(cls):
        return cls.query.filter().all()

    def query_dict_code(dict_code):
        return Dictitem.query.filter(Dictitem.dict_code == dict_code).first()

    def add_to_db(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()
