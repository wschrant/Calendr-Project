from rest_framework import serializers
from . models import *
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure password is write-only

    class Meta:
        model = User
        fields = [
            'id',
            'first_name', 
            'last_name', 
            'email', 
            'username', 
            'password', 
            'image', 
            'role', 
            'created_date', 
            'updated_date'
        ]
        read_only_fields = ['created_date', 'updated_date']

    def create(self, validated_data):
        # Use set_password to hash the password
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # Handle password update separately
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class GroupSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Group
        fields = [
            "id",
            "name", 
                "description",
                "image",
                "created_date", 
                "updated_date"]
        read_only_fields = ['created_date', 'updated_date']

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta: 
        model = GroupMember
        fields = [
            "id",            
            "rank", 
                "group", 
                "user", 
                "created_date", 
                "updated_date"]
        read_only_fields = ['created_date', 'updated_date']

class ToDoPostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ToDoPost
        fields = [
            "id",            
            "title", 
                "content", 
                "date", 
                "time", 
                "user", 
                "group",
                "created_date", 
                "updated_date"]
        read_only_fields = ['created_date', 'updated_date']

    def validate_date(self, value):
        """Ensure the date is not in the past."""
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError("The date cannot be in the past.")
        return value