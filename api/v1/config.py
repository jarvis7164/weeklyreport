#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 9:54
# @Author  : jarvis
# @File    : config.py
# @Software: PyCharm
# @Contact : 309194437@qq.com
"""数据库相关配置"""
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/weeklyreport?charset=UTF8MB4"

# SQLAlchemy 将会记录所有发到标准输出(stderr)的语句，这对调试很有帮助。
SQLALCHEMY_ECHO = True

# Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
SQLALCHEMY_TRACK_MODIFICATIONS = True