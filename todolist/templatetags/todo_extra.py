from django import template
from datetime import datetime, date
from ..models import Todos
from django.utils import dateformat
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def type_div(id):
    todo = Todos.objects.get(id=id)
    days = days_until(todo.date_finished)

    if todo.done:
        if days > 0:
            return mark_safe(f"<div id='todo-{id}' data-pk='{id}' class='row row-cols-5 no-gutters alert alert-success align-items-center' style='border: solid 1px #CDCDCD'>")
        else:
            return mark_safe(f"<div id='todo-{id}' data-pk='{id}' class='row row-cols-5 no-gutters alert alert-warning align-items-center' style='border: solid 1px #CDCDCD'>")
    else:
        if days > 0:
            return mark_safe(f"<div id='todo-{id}' data-pk='{id}' class='row row-cols-5 no-gutters alert alert-light align-items-center' style='border: solid 1px #CDCDCD'>")
        else:
            return mark_safe(f"<div id='todo-{id}' data-pk='{id}' class='row row-cols-5 no-gutters alert alert-danger align-items-center' style='border: solid 1px #CDCDCD'>")

register.filter('type_div', type_div)

@register.filter
def days_until(input_date):
    delta = datetime.date(input_date) - datetime.now().date()
        
    return delta.days

register.filter('days_until', days_until)

@register.filter
def days_since(input_date):
    delta = datetime.now().date() - datetime.date(input_date)

    return delta.days

register.filter('days_since', days_since)