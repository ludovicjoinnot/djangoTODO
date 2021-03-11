import requests
from django.http import HttpResponse
from django.shortcuts import render
import pymysql


def index(request):
    context = {}
    if request.method == 'POST':
        print(request.POST['title'])
        r = requests.post('https://jsonplaceholder.typicode.com/todos/', params=request.POST)
        print(r.json())
        context = { 'attributs': r.json() }
    elif request.method == 'PUT':
        print(request.PUT['id'])
        r = requests.post('https://jsonplaceholder.typicode.com/todos/', params=request.PUT)
        print(r.json())
        context = { 'modifications': r.json() }
    else:
        if request.GET.get('id') == '':
            r = requests.get('https://jsonplaceholder.typicode.com/todos/')
            print(r.json())
            context = {'lecture': r.json()}
        else:
            r = requests.get('https://jsonplaceholder.typicode.com/todos/', params=request.GET)
            print(r.json())
            context = {'lecture': r.json()}
    return render(request, 'index.html', context=context)


# def connexion(request):
#     host = 'dba.clhjln4zga20.eu-central-1.rds.amazonaws.com'
#     user = 'root'
#     password = 'Cartesoft_1'
#     database = 'aws'
#
#     db = pymysql.connect(host, user, password, database)
#     with db:
#         cur = db.cursor()
#         cur.execute("SELECT VERSION()")
#         version = cur.fetchone()
#         print("Database version: {} ".format(version[0]))
#
#     sql = '''drop database aws'''
#     cur.execute(sql)
#     sql = '''create database aws'''
#     cur.execute(sql)
#
#     cur.connection.commit()
#     sql = '''use database aws'''
#     cur.execute(sql)
#
#     sql = '''
#     create table todo (
#     id int not null auto_increment,
#     title text,
#     completed boolean
#     )
#     '''
#     cur.execute(sql)
#
#     sql = '''show tables'''
#     cur.execute(sql)
#     cur.fetchall()
#
#     sql = '''
#         insert into todo(title, completed) values('%s','%s')''' % ('test',True)
#     cur.execute(sql)
#     db.commit()
#
#     sql = '''select * from todo'''
#     cur.execute(sql)
#     cur.fetchall()
#     return render(request, 'index.html')
