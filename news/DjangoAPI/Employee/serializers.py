from rest_framework import serializers
from .models import User, Post
from django.contrib.auth.hashers import make_password  

class UserRegistrationSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [ '_id' ,'id', 'username', 'email', 'password' , 'role' ]

    password = serializers.CharField(write_only=True)

    def get__id(self, obj):
        return str(obj._id)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.password = make_password(password)  
        user.save()
        return user
    

class UserFindSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [ '_id' , 'username', 'email', 'password' ]

    password = serializers.CharField(write_only=True)

    def get__id(self, obj):
        return str(obj._id)
    



class PostSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()  # Конвертація ObjectId у рядок

    class Meta:
        model = Post
        fields = ['_id', 'title', 'content', 'author', 'created_at']

    def get__id(self, obj):
        return str(obj._id)
    
    def get_author(self, obj):
        return str(obj.author)