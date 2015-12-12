from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Todo
from django.contrib.auth.models import User

# Create your views here.


def todolists(request):
	waitingtodos = Todo.objects.filter(flag=1)
	finishedtodos = Todo.objects.filter(flag=0)
	return render(request,"mytodo/todolist.html",{"waitingtodos":waitingtodos,"finishedtodos":finishedtodos})

def newfinishedtodo(request,id):
	newfinishedtodo = Todo.objects.get(id=id)
	if newfinishedtodo.flag=='1':
		newfinishedtodo.flag='0'
		newfinishedtodo.save()
	return HttpResponseRedirect("/todolists/")

def rebacktodo(request,id):
	rebacktodo = Todo.objects.get(id=id)
	if rebacktodo.flag=='0':
		rebacktodo.flag='1'
		rebacktodo.save()
	return HttpResponseRedirect("/todolists/")

def addtodo(request):
	if request.method == 'POST':
		todo = request.POST['todo']
		priority = request.POST['priority']
		user = User.objects.get(id=1)
		addtodo = Todo(user=user, todo=todo, priority=priority, flag='1')
		addtodo.save()
		todolist = Todo.objects.filter(flag=1)
		finishtodos = Todo.objects.filter(flag=0)
		return HttpResponseRedirect("/todolists/")

		
def deltodo(request,id):
	deltodo = Todo.objects.get(id=id)
	deltodo.delete()
	return HttpResponseRedirect("/todolists/")


def updatetodo(request,id):
	oldtodo = Todo.objects.get(id=id)
	if request.method == 'POST':
		oldtodo.todo = request.POST['todo']
        oldtodo.priority = request.POST['priority']
        oldtodo.save()
        return HttpResponseRedirect("/todolists/")









	