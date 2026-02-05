from rest_framework import serializers
from .models import User,UserProfile, AbstractUser, Post, Tag

class UserSerializers(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['id', 'created_at', 'updated_at', 'groups', 'user_permissions',]

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class RegisterUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['first_name', "last_name", "username", "email", "password",]

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password",]

class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"