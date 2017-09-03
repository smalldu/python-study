#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from flask import Flask,session,url_for,flash
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask import render_template
from flask_bootstrap import Bootstrap


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_script import Manager
from flask_moment import Moment


app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is a secret key'


#  引入 bootstrap
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)


@app.route('/', methods = ['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('it seemed that you have change your name')
		session['name'] = form.name.data  # 将数据存在session中
		return redirect(url_for('index'))
	return render_template('index.html',form = form , name = session.get('name'))

class Human():
	def someMethod(self):
		return 'Flask Hello world ! '
		

@app.route('/user/<name>')
def user(name):
	myDict = {'key':'This is a Flask Program'}
	myList = ['it','swift','python','flask']
	myIntvar = 1
	myObj = Human()
	return render_template('user.html',name = name,myDict = myDict,myList = myList,myIntvar =  myIntvar,myObj = myObj)

@app.route('/macro')
def macro():
    comments = ['it', 'Hello', 'the', 'world']
    return render_template('macro.html', comments=comments)


@app.route('/bootstrap/<name>')
def bootstrap(name):
    return render_template('bootstrap.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



# ********** 表单 *********** 

class NameForm(FlaskForm):
	name = StringField('What is your name? ' , validators=[Required()])
	submit = SubmitField('Submit')


if __name__ == '__main__':
    app.run()

