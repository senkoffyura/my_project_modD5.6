from django.contrib import admin
from .models import Category, Post, Subscription, PostCategory


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Subscription)
admin.site.register(PostCategory)