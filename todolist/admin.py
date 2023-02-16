from django.contrib import admin
from .models import Lists, Todos, Users

# Register your models here.
class TodoInline(admin.TabularInline):
    model = Todos
    extra = 3

# Todo list database
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'datetime_created',)
    inlines = [TodoInline]

admin.site.register(Lists, TodoListAdmin)

# User database
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)

admin.site.register(Users, UserAdmin)