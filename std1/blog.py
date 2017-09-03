#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


from flask import Flask
from sshtunnel import SSHTunnelForwarder
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# SSH 安全访问 
server =  SSHTunnelForwarder(
     ('118.190.149.137', 22),
     ssh_password="smalldu.223",
     ssh_username="root",
     remote_bind_address=('127.0.0.1', 3306))

server.start() #start ssh sever
print('Server connected via SSH')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:smalldu223@127.0.0.1:%s/blog' % server.local_bind_port
db = SQLAlchemy(app)




class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(180))
    content = db.Column(db.String(320))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<Blog %r>' % self.title



blogs = Blog.query.all()
print(blogs)

server.stop()