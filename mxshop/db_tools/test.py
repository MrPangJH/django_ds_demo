#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 下午11:39
# @Author  : CoderP
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+"../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mxshop.mxshop.settings")

import django
django.setup()

from goods.models import GoodsCategory

from mxshop.db_tools.data.category_data import row_data

get_all = GoodsCategory.objects.all()

print(get_all)