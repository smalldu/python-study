#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/user/<name>')
def user(name):
	user_agent = request.headers.get('User-Agent')
	return '<H1>Hello , %s . Your Browser is %s  </H1>' % (name,user_agent) , 400 # 可以直接设置状态吗

@app.route('/red')
def red():
    return redirect('http://www.baidu.com') # 重定向 


@app.route('/doc')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/get/<id>')
def get_id(id):  # 只有输入9 才能得到正确的页面 其他会报404
    if id != '9':
        abort(404)
    return '<h1>Hello, %s!</h1>' % id
	
if __name__ == '__main__': # python 的惯用法 确保执行此脚本时才启动服务器
    app.run()






















