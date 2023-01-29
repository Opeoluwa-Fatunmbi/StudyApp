#import datetime
import datetime
from django.db import models
from django.contrib.auth.models import User




# Create your models here.


class Topic(models.Model):
    #name =  models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)



    def __str__(self) -> str:
        return self.name





class Room(models.Model):
    #host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='hosted_rooms')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    #name = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    description = models.TextField(null=True, blank=True)
    #participants = models.ManyToManyField(User)
    participants = models.ManyToManyField(User, related_name='participating_rooms')
    updated = models.DateTimeField(auto_now=True)
    #created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)






    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    #name =  models.ForeignKey(User, on_delete=models.CASCADE)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages', default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    #created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(default=datetime.datetime.now)




    def __str__(self) -> str:
        return self.body[0:50]
