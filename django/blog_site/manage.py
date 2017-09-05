#!/usr/bin/env python
import os
import sys


# 一个实用的命令行，用来与你的项目进行交互。它是一个对django-admin.py工具的简单封装。你不需要编辑这个文件。

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_site.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
