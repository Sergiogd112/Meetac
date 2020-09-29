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
    lastlogin=models.DateTimeField(auto_now=True)


class Message(models.Model):
    id_sender = models.ForeignKey(MeetacUser, on_delete=models.CASCADE,related_name='sender')
    id_receiver = models.ForeignKey(MeetacUser, on_delete=models.CASCADE,related_name='reciever')
    type = models.CharField(max_length=32, default='text')
    body = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now=True)
    recieved = models.BooleanField(default=False)
    read = models.BooleanField(default=False)


class Graph_history(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    graph = models.TextField(blank=True)


class Tag_history(models.Model):
    name = models.CharField(max_length=32)
    count = models.IntegerField(default=0)

class Tag(models.Model):
    tag= models.ForeignKey(Tag_history,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Selected(models.Model):
    chooser = models.ForeignKey(MeetacUser, on_delete=models.CASCADE,related_name='chooser')
    choosed = models.ForeignKey(MeetacUser, on_delete=models.CASCADE, related_name='choosed')
    datetime = models.DateTimeField(auto_now=True)


class Match(models.Model):
    user1 = models.ForeignKey(MeetacUser, on_delete=models.CASCADE,related_name='user1')
    user2 = models.ForeignKey(MeetacUser, on_delete=models.CASCADE, related_name='user2')


class Reports(models.Model):
    reported = models.ForeignKey(MeetacUser, on_delete=models.CASCADE)
    cause = models.CharField(max_length=32)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=True)


class Views(models.Model):
    viewer = models.ForeignKey(MeetacUser, on_delete=models.CASCADE, related_name='viewer')
    viewed = models.ForeignKey(MeetacUser, on_delete=models.CASCADE, related_name='viewed')
    datetime = models.DateTimeField(auto_now=True)
    time = models.IntegerField(default=0)
