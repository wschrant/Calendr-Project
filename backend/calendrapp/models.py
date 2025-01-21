from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=40)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Group(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class GroupMember(models.Model):
    rank = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class ToDoPost(models.Model):
    title = models.CharField(max_length=255) 
    content = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)