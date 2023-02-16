from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime
import json

from .models import Todos, Lists, Users
from .forms import AddTodoForm, AddTodoListForm

# Create your views here.
def Todo(request, id_list, id_todo):
    todo = Todos.objects.get(id=id_todo)
    template = loader.get_template('todo.html')
    context = {
        'id': todo.id,
        'name': todo.name,
        'description': todo.description,
        'deadline': todo.date_finished,
    }
    return JsonResponse(context)

# Single list view
def TodoList(request, id_list):
    todoList = Lists.objects.get(id=id_list)
    todos = Todos.objects.filter(list=id_list).order_by('position')

    form = AddTodoForm()

    today = datetime.now().date()

    template = loader.get_template('todolist.html')
    context = {
        'list': todoList,
        'todos': todos,
        'form': form,
        'today':today,
    }
    return HttpResponse(template.render(context, request))

def TodoLists(request):
    todoLists = Lists.objects.all()
    template = loader.get_template('todolists.html')

    form = AddTodoListForm()

    context = {
        'lists': todoLists,
        'today': datetime.now(),
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def Main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

#
# DATABASE VIEWS FOR TODO TASKS
#

@require_http_methods(['POST'])
def TodoDone(request, id_list, id_todo):
    todo = Todos.objects.get(id=id_todo)

    if todo.done:
        todo.done = False
    else:
        todo.done = True
    todo.save()
    todos = Todos.objects.all()

    delta_days = datetime.date(todo.date_finished) - datetime.now().date()
    delta_days = delta_days.days

    class_alert = ''

    if(todo.done):
        if(delta_days > 0):
            class_alert = 'alert-success'
        else:
            class_alert = 'alert-warning'
    else:
        if(delta_days > 0):
            class_alert = 'alert-light'
        else:
            class_alert = 'alert-danger'

    return HttpResponse(class_alert)

@require_http_methods(['POST'])
def deleteTodo(request, id_list, id_todo):
    Todos.objects.get(id=id_todo).delete()
    return HttpResponseRedirect(f'/lists/{id_list}/')

@require_http_methods(['POST'])
def newTodo(request, id_list):
    form = AddTodoForm(request.POST)

    if form.is_valid():
        # TODO Blijven op de pagin
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        date_finished = form.cleaned_data['date_finished']

        new_todo = Todos.objects.create(list_id=id_list, name=name, description=description, date_finished=date_finished)
        return HttpResponseRedirect(f'/lists/{id_list}/')
    else:
        form = AddTodoForm()

@require_http_methods(['POST'])
def changeTodo(request, id_list, id_todo):
    form = AddTodoForm(request.POST)

    if form.is_valid():
        # TODO Blijven op de pagin
        try:
            todo = Todos.objects.get(id=id_todo)
            print(todo)
            todo.name = form.cleaned_data['name']
            todo.description = form.cleaned_data['description']
            todo.date_finished = form.cleaned_data['date_finished']

            todo.save()
            return HttpResponseRedirect(f'/lists/{id_list}/')
        except ObjectDoesNotExist:
            print('Object does not exist')
    else:
        form = AddTodoForm()

@require_http_methods(['POST'])
def sortTodo(request, id_list):
    todos = json.loads(request.POST.get('sort'))
    for todo in todos:
        todo_object = get_object_or_404(Todos, pk=int(todo['pk']))
        todo_object.position = todo['order']
        todo_object.save()
    return HttpResponse('saved')

#
# DATABASE VIEWS FOR TODO LISTS
#

@require_http_methods(['POST'])
def addList(request):
    form = AddTodoListForm(request.POST)

    if form.is_valid():
        # TODO blijven op de pagina
        name = form.cleaned_data['name']
        desc = form.cleaned_data['description']
        user = Users.objects.get(id=1)

        Lists.objects.create(name=name, description=desc, user=user)
    return HttpResponseRedirect(f'/lists/')

@require_http_methods(['POST'])
def deleteList(request, id_list):
    Lists.objects.get(id=id_list).delete()
    return HttpResponseRedirect(f'/lists/')

@require_http_methods(['POST'])
def changeList(request, id_list):
    form = AddTodoListForm(request.POST)

    if form.is_valid():
        # TODO Blijven op de pagin
        try:
            list = Lists.objects.get(id=id_list)
            list.name = form.cleaned_data['name']
            list.description = form.cleaned_data['description']

            list.save()
            return HttpResponseRedirect('/lists/')
        except ObjectDoesNotExist:
            print('Object does not exist')
    else:
        form = AddTodoForm()

@require_http_methods(['GET'])
def getList(request, id_list):
    if request.method == 'GET':
        todoList = Lists.objects.get(id=id_list)

        id = id_list
        name = todoList.name
        desc = todoList.description

        context = {
            'id': id,
            'name': name,
            'description': desc,
        }
        return JsonResponse(context)