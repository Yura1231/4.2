

from djongo import models
from bson.objectid import ObjectId


class User(models.Model):
    

    ADMIN = 'admin'  
    USER = 'user'    

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]

    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=USER)

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    contact_info = models.CharField(max_length=255, null=True, blank=True)

    @property
    def id(self):
        return str(self._id)

    def __str__(self):
        return self.username
    


class Post(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name='posts')  # Автор поста
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title