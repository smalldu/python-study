### 在 Flask 中有两种上下文：程序上下文和请求上下文，这两种上下文提供的变量如下：

- current_app   程序上下文   当前激活程序的程序实例
- g 程序上下文   处理请求时用作临时存储的对象，每次请求都会重设这个变量
- request   请求上下文   请求对象，封装了客户端发出的 HTTP 请求中的内容
- session   请求上下文   用户绘画，用户存储请求之间需要“记住”的值的字典
- Flask 会在分发请求之前激活程序和请求上下文，请求处理完成后再将其删除

### 请求钩子

>有时在处理请求之前或者之后执行代码会很有用，Flask 提供了注册通用函数的功能，注册的函数可在请求被分发到视图函数之前或之后调用。请求钩子使用修饰器实现。Flask 支持以下四种钩子：

- before_first_request    注册一个函数，在处理第一个请求之前运行
- before_request  注册一个函数，在每次请求之前运行
- after_request   注册一个函数，如果没有未处理的异常抛出，在每次请求后运行
- teardown_request    注册一个函数，即使有未处理的异常抛出，也在每次请求后运行

Flask 会在分发请求之前激活程序和请求上下文，请求处理完成后再将其删除 
在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量g

### 响应 

>Flask 调用视图函数后，会将其返回值作为响应的内容。如果视图函数返回的响应需要使用不同的状态码，那么可以把数字代码作为第二个返回值，添加到响应文本之后。

添加状态码 

```python
def index():
    return '<p>Bad Request !</p>', 400
```

如果不想返回由多个值组成的元组，Flask 视图函数还可以返回 Response 对象。make_response() 函数可接受1/2/3个参数，并返回一个 Response 对象


还有一种特殊的响应由 abort 函数生成，用于错误处理

```python
@app.route('/get/<id>')
def get_id(id):
    if id != '9':
        abort(404)
    return '<h1>Hello, %s!</h1>' % id
```


# Jinja 2 模版引擎 

### 渲染模版

>默认情况下，Flask 在程序文件夹中的 templates 子文件夹中寻找模版

```py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')


def index():
    return render_template('index.html')


@app.route('/user/<name>')


def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()
```

这段代码可以和上面实现相同的作用，render_template()函数的第一个参数是模版的文件名，随后的参数都是键值对，表示模版中变量对应的真实值

### 变量

>模版中使用的{{ name }}结构表示一个变量，它是一种特殊的占位符，告诉模版引擎这个位置的值从渲染模版时使用的数据中获取 
Jinja2 能识别所有类型的变量，甚至是一些复杂的类型，例如列表、字典和对象，例如

```python
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value froma list: {{ mylist[3] }}.</p>
<p>A value froma list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value froman object's method: {{ myobj.somemethod() }}.</p>
```

也可以使用过滤器来修改变量，过滤器名添加在变量名之后，中间使用竖线分隔
过滤器名    说明
safe    渲染值时不转义
capitalize  把值的首字母转换成大写，其他字母转换成小写
lower   把值转换成小写形式
upper   把值转换成大写形式
title   把值中的每个单词的首字母都变成大写
trim    把值的首尾空格去掉
striptags   渲染前把值中的 HTML 标签都删掉
默认情况出于安全考虑， Jinja2 会转义所有变量，完整的过滤器可去 Jinja2 的文档中查看

### 控制结构

>Jinja2 提供了多种控制结构，可用来改变模版的渲染流程

```html
{{ % if user %}}
    hello, {{ user }}
{{% else %}}
    hello, world
{{% endif % }}
```

```html
{% for comment in comments %}
    <li>{{ comment }}</li>
{% endfor %}
```

extends指令声明这个模版衍生自base.html，在此指令后基模版的三个块被重新定义，模版引擎会将其插入适当的位置，使用super()来获取原来的内容

request.from 能获取 POST 请求中提交的表单数据

# Web 表单

### 跨站请求伪造保护

>默认情况下，Flask-WTF 能保护所有表单免受跨站请求伪造的攻击，为了实现 CSRF 保护，Flask-WTF 需要程序设置一个密钥，会使用这个密钥生成加密令牌，再用令牌验证请求中表单数据的真伪 


设置密钥的方法如示例所示

```
app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is a secret key'
```

>为了增强安全性，密钥不应该直接写入代码，而要保存在环境变量中

### 表单类

>使用 Flask-WTF 时，每个 Web 表单都由一个继承自 Form 的类表示，这个类定义表单中的一组字段，每个字段都用对象表示，字段对象可附属一个或多个验证函数


表单的每个属性都定义为类的属性，类变量的值是相应字段类型的对象，StringField 类表示属性为 type="text" 的 元素，SubmitField 类表示属性为 type="submit" 的 元素 

字段构造函数的第一个参数是把表单渲染成 HTML 时使用的标号，可选参数 validators 指定一个由验证函数组成的列表，在接受用户提交的数据之前验证数据，验证函数Required()确保提交的字段不为空

### 重定向和用户会话

 ### Flash 消息
 





















