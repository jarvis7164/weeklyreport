# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 9:52
# @Author  : jarvis7164
# @File    : urls.py
# @Software: PyCharm
# @Contact : 309194437@qq.com
from flask import render_template, send_file

from api.v1.views import *

# api.add_resource(Hello, '/')
api.add_resource(Login, '/api/v1/login')
api.add_resource(Tasklist, '/api/v1/task')
api.add_resource(QueryTasklist, '/api/v1/query')
api.add_resource(UserList, '/api/v1/users')
api.add_resource(RoleList, '/api/v1/roles')
api.add_resource(DepartmentList, '/api/v1/departments')
api.add_resource(ProductList, '/api/v1/products')
api.add_resource(DictitemList, '/api/v1/dictitem')
api.add_resource(Dictitem_query, '/api/v1/dictitem/query')
api.add_resource(Weeklyreport_output, '/api/v1/weeklyreport_output')
api.add_resource(Weeklyreport_download, '/api/v1/weeklyreport_download')
api.add_resource(Pre_condition, '/api/v1/precondition')
api.add_resource(QueryPreconditon, '/api/v1/querypreconditon')


@app.route('/')
def index():
    # return render_template('index.html',submenu = 1,item =1)
    return send_file('./templates/index.html')  #使用该方法可以跟直接打开本地html差不多，不适用jinja2方式

@app.route('/login')
def index_login():
    # return render_template('login.html')
    return send_file('./templates/login.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)
