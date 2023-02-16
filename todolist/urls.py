from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='main'),
    path('lists/', views.TodoLists, name='todo_lists'),
    path('lists/add-list/', views.addList, name='add-list'),
    path('lists/get-<int:id_list>/', views.getList, name='change-list'),
    path('lists/change-<int:id_list>/', views.changeList, name='change-list'),
    path('lists/delete-<int:id_list>/', views.deleteList, name='delete-list'),
    path('lists/<int:id_list>/', views.TodoList, name='todo_list'),
    path('lists/<int:id_list>/<int:id_todo>/', views.Todo, name='todo_detail'),
    path('lists/<int:id_list>/<int:id_todo>-done/', views.TodoDone, name='todo_done'),
    path('lists/<int:id_list>/new-todo/', views.newTodo, name='new-todo'),
    path('lists/<int:id_list>/sort-todo/', views.sortTodo, name='sort-todo'),
    path('lists/<int:id_list>/change-<int:id_todo>/', views.changeTodo, name='change-todo'),
    path('lists/<int:id_list>/delete-<int:id_todo>/', views.deleteTodo, name='delete-todo'),
]