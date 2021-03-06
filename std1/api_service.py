#!/usr/bin/env python3
# -*- coding: utf-8 -*- 


from flask import Flask, request, jsonify
from restfultools import *

app = Flask(__name__)


#这是数据源
datas = [
		{'name': 'javascript', 'useto': 'web development'} ,
	    {'name': 'python', 'useto': 'do anything'} ,
	    {'name': 'php', 'useto': 'web development'} ,
	    {'name': 'c++', 'useto': 'web server'}
    	]

#获取所有的资源  注意我用了复数形式的url
@app.route('/languages')
def getAll():
    return fullResponse(R200_OK, datas)


@app.route('/languages/<string:name>')
def getOne(name):
	result = [data for data in datas if data['name'] == name]
	if len(result) == 0:
		return statusResponse( R404_NOTFOUND)
	return fullResponse(R200_OK,result[0])

#POST请求，增加一项
@app.route('/language', methods=['POST'])
def addOne():
    request_data = request.get_json()
    if not 'name' in request_data or not 'useto' in request_data:
        return statusResponse(R400_BADREQUEST)
    name = request_data['name']
    useto = request_data['useto']
    datas.append({'name': name, 'useto': useto})
    return statusResponse(R201_CREATED)


#PUT，PATCH 更新资源
#按照RestFul设计：
#PUT动作要求客户端提供改变后的完整资源
#PATCH动作要求客户端可以只提供需要被改变的属性
#在这里统一使用PATCH的方法
@app.route('/language/<string:name>', methods=['PUT', 'PATCH'])
def editOne(name):
    result = [data for data in datas if data['name'] == name]
    if len(result) == 0:
        return statusResponse(R404_NOTFOUND)
    request_data = request.get_json()
    if 'name' in request_data:
        result[0]['name'] = request_data['name']
    if 'useto' in request_data:
        result[0]['useto'] = request_data['useto']
    return statusResponse(R201_CREATED)


#DELETE删除，没什么好说的
@app.route('/language/<string:name>', methods=['DELETE'])
def delOne(name):
    result = [data for data in datas if data['name'] == name]
    if len(result) == 0:
        return statusResponse(R404_NOTFOUND)
    datas.remove(result[0])
    return statusResponse(R204_NOCONTENT)

if __name__ == '__main__':
    app.run()