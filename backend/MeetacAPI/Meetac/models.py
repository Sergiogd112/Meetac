from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser

class MeetacUser(AbstractBaseUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tags = models.TextField(blank=True)
    policy = models.BooleanField(default=False)
    birthday = models.DateField()
    description = models.TextField(max_length=256)
    profileimg = models.ImageField()
    banned = models.IntegerField(default=0)


class Message(models.Model):
    id_sender = models.ForeignKey(User)
    id_receiver = models.ForeignKey(User)
    type = models.CharField(max_length=32, default='text')
    body = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now=True)
    recieved = models.BooleanField(default=False)
    read = models.BooleanField(default=False)


class Graph_history(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    graph = models.TextField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=32)
    users = models.ManyToManyField(User)
    count = models.IntegerField(default=0)


class Selected(models.Models):
    chooser = models.ForeignKey(User)
    choosed = models.ForeignKey(User)
    datetime = models.DateTimeField(auto_now=True)

class Match(models.Models):
    user1=models.ForeignKey(User)
    user2= models.ForeignKey(User)

class Reports(models.Models):
    reported=models.ForeignKey(User)
    cause=model.CharField(max_lenght=32)
    description= models.TextField()
    datetime=models.DateTimeField(auto_now=True)

class Views(models.Model):
    viewer=models.ForeignKey(User)
    viewed= models.ForeignKey(User)
    datetime=models.DateTimeField(auto_now=True)
    time=models.IntegerField(default=0)