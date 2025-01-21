from rest_framework import serializers
from . models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 
                  'last_name', 
                  'email', 
                  "username", 
                  "password", 
                  "image",
                  "type", 
                  "created_date", 
                  "updated_date"]

class GroupSerializer(serializers.ModelSerializer):
    class Meta: Group
    fields = ["name", 
              "content",
              "image",
              "created_date", 
              "updated_date"]

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta: GroupMember
    fields = ["rank", 
              "group", 
              "user", 
              "created_date", 
              "updated_date"]

class ToDoPostSerializer(serializers.ModelSerializer):
    class Meta: ToDoPost
    fields = ["title", 
              "content", 
              "date", 
              "time", 
              "user", 
              "group" 
              "created_date", 
              "updated_date"]