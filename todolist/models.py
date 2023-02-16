from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
# TODO Create choices of what kind of todo it is
class Users(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    datetime_created = models.DateTimeField(default=timezone.now, editable=True)

    def __unicode__(self):
        return u'%s' % (self.username)

class Lists(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(default=timezone.now, editable=True)

class Todos(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    done = models.BooleanField(default=False)
    list = models.ForeignKey(Lists, on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(default=timezone.now, editable=True)
    date_finished = models.DateTimeField(null=False)
    position = models.IntegerField(default=0)