import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pymysql

from todolist.forms import TaskForm
from todolist.models import Task

'''def index(request):
    context = {}
    if request.method == 'POST':
        print(request.POST['title'])
        r = requests.post('https://jsonplaceholder.typicode.com/todos/', params=request.POST)
        print(r.json())
        context = { 'attributs': r.json() }
    elif request.method == 'PUT':
        print(request.PUT['id']+"put")
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
            context = {'modifications': r.json()}
    return render(request, 'BUIndex.html', context=context)'''

def index(request):
    context = {}
    if request.method == "POST":
        # Get the posted form
        form = TaskForm(request.POST)
        if form.is_valid():
            #form.save() #version DB
            r = requests.post('https://jsonplaceholder.typicode.com/todos/', params=request.POST)
            print(r.json())
        return redirect("index")
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos/')
    print(tasks.json())
    context = {'tasks': tasks.json()}
    return render(request, "index.html", context=context)


def update_task(request, pk):
    #Récup le todo
    task = requests.get('https://jsonplaceholder.typicode.com/todos/'+str(pk))
    print(task.json())
    context = {'task': task.json()}
    if request.method == "POST":
        r =requests.put('https://jsonplaceholder.typicode.com/todos/', params=request.POST)
        print(r.json())
        return redirect("index")
    return render(request, "update_task.html", context=context) #, {"task_edit_form": r}


def delete_task(request, pk):
    task = requests.delete('https://jsonplaceholder.typicode.com/todos/'+str(pk))
    print(task.json())
    return redirect("index")



### VERSION SANS API ####
#
# def index(request):
#     form = TaskForm()
#     if request.method == "POST":
#         # Get the posted form
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("index")
#     tasks = Task.objects.all() # add this
#     return render(request, "index.html", {"task_form": form, "tasks": tasks})
#
#
# def update_task(request, pk):
#     task = Task.objects.get(id=pk)
#
#     form = TaskForm(instance=task)
#
#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             form.save()
#             return redirect("index")
#
#     return render(request, "update_task.html", {"task_edit_form": form})
#
#
#
# def delete_task(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#     return redirect("index")

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
#     return render(request, 'BUIndex.html')
