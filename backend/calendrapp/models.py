from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
    
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField('Email', max_length=100, unique=True)
    image = models.ImageField('User Image', null=True, blank=True, upload_to='user_images/')
    role = models.CharField('Role', max_length=40, default='user')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name



class Group(models.Model):
    name = models.CharField('Group Name', max_length=255)
    description = models.TextField('Description', blank=True)
    image = models.ImageField('Group Image', null=True, upload_to='group_images/', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class GroupMember(models.Model):
    rank = models.CharField('Group Rank', max_length=100, choices=[
        ('admin', 'Admin'),
        ('member', 'Member')
    ])
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rank

class ToDoPost(models.Model):
    title = models.CharField('Title', max_length=255) 
    content = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title