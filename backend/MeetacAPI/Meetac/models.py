from django.db import models
from django.contrib.auth.models import User


class MeetacUser(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tags = models.JSONField(blank=True)
    policy = models.BooleanField(default=False)
    birthday = models.DateField()
    description = models.TextField(max_length=256)
    profileimg = models.ImageField()
    selected = models.JSONField(blank=True)
    matches = models.JSONField(blank=True)
    banned = models.IntegerField(default=0)
    reported = models.JSONField(blank=True)
    viewed = models.JSONField(blank=True)


class Message(models.Model):
    id_sender = models.ForeignKey(MeetacUser)
    id_receiver = models.ForeignKey(MeetacUser)
    type = models.CharField(max_length=32, default='text')
    body = models.JSONField(blank=True)
    datetime = models.DateTimeField(_, auto_now=True, auto_now_add=False)
    recieved = models.BooleanField(default=False)
    read = models.BooleanField(default=False)


class Graph_history(models.Model):
    date_time = models.DateTimeField(_, auto_now=True, auto_now_add=False)
    graph = models.JSONField(blank=True)
