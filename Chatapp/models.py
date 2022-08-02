from datetime import datetime
from operator import mod
from pyexpat import model
from django.db import models

class Group(models.Model):
    name=models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class E_Group(models.Model):
    e_maker = models.CharField(max_length=150, default='')
    e_name= models.CharField(max_length=100, default='i')


    def __str__(self):
        return self.e_name


class Message(models.Model):
    group = models.CharField(max_length=120, default='')
    senter = models.CharField(max_length=150, default='')
    msg = models.TextField()
    crt_time = models.DateTimeField(default=datetime.now())