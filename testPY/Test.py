# -*- coding:utf-8 -*-
import requests
import json
import qrcode




movies = [
    {'title': '安卓测试最新包', 'year': 'pkgname'}
]




umb1=movies[0].get('title')
movies[0]['year']='213'
umb2=movies[0]['year']

print (umb1,umb2)