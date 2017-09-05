##  安装 virtualenv

```sh
pip install virtualenv
```

```sh
virtualenv my_env
```

```sh
which python3
```

```
virtualenv my_env -p /Library/Frameworks/Python.framework/Versions/3.5/bin/python3
```

通过以下命令来激活你的virtualenv：
```
source my_env/bin/activate
```
你可以使用deactivate命令随时停用你的virtualenv。


我们的第一个项目将会是一个完整的blog站点。Django提供了一个命令允许你方便的创建一个初始化的项目文件结构。在终端中运行以下命令：

django-admin startproject mysite

这些初始应用表将会在数据库中创建。过一会儿你就会学习到一些关于migrate的管理命令。
python manage.py migrate 


>Django自带一个轻量级的web服务器来快速运行你的代码，不需要花费额外的时间来配置一个生产服务器。当你运行Django的开发服务器，它会一直检查你的代码变化。当代码有改变，它会自动重启，将你从手动重启中解放出来。但是，它可能无法注意到一些操作，例如在项目中添加了一个新文件，所以你在某些场景下还是需要手动重启。

python manage.py runserver

你可以指定Django在定制的host和端口上运行开发服务，或者告诉它你想要运行你的项目通过读取一个不同的配置文件。例如：你可以运行以下 manage.py命令：
python manage.py runserver 127.0.0.1:8001 \
--settings=mysite.settings

>这个命令迟早会对处理需要不同设置的多套环境启到作用。记住，这个服务器只是单纯用来开发，不适合在生产环境中使用。为了在生产环境中部署Django，你需要使用真实的web服务让它运行成一个WSGI应用例如Apache，Gunicorn或者uWSGI（译者注：强烈推荐 nginx+uwsgi+Django）

- DEBUG 一个布尔型用来开启或关闭项目的debug模式。如果设置为True，当你的应用抛出一个未被捕获的异常时Django将会显示一个详细的错误页面。当你准备部署项目到生产环境，请记住一定要关闭debug模式。永远不要在生产环境中部署一个打开debug模式的站点因为那会暴露你的项目中的敏感数据。
- ALLOWED_HOSTS 当debug模式开启或者运行测试的时候不会起作用（译者注：最新的Django版本中，不管有没有开启debug模式该设置都会启作用）。一旦你准备部署你的项目到生产环境并且关闭了debug模式，为了允许访问你的Django项目你就必须添加你的域或host在这个设置中。
- INSTALLED_APPS这个设置你在所有的项目中都需要编辑。这个设置告诉Django有哪些应用会在这个项目中激活。默认的，Django包含以下应用：
    - django.contrib.admin：这是一个管理站点。
    - django.contrib.auth：这是一个权限框架。
    - django.contrib.contenttypes：这是一个内容类型的框架。
    - django.contrib.sessions：这是一个会话（session）框架。
    - django.contrib.messages：这是一个消息框架。
    - django.contrib.staticfiles：这是一个用来管理静态文件的框架

- MIDDLEWARE_CLASSES 是一个包含可执行中间件的元组。
- ROOT_URLCONF 指明你的应用定义的主URL模式存放在哪个Python模块中。
- DATABASES 是一个包含了所有在项目中使用的数据库的设置的字典。里面一定有一个默认的数据库。默认的配置使用的是SQLite3数据库
- LANGUAGE_CODE 定义Django站点的默认语言编码

下面创建第一个应用
python manage.py startapp blog


python manage.py makemigrations blog
python manage.py sqlmigrate blog 0001

创建一个超级用户
python manage.py createsuperuser





































































