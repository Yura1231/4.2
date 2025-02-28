from django.contrib import admin
from .models import User, Post


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'created_at')  
    search_fields = ('username', 'email')  
    list_filter = ('role', 'created_at')  

admin.site.register(User, UserAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  
    search_fields = ('title', 'author__username')  
    list_filter = ('created_at',)  

admin.site.register(Post, PostAdmin)
