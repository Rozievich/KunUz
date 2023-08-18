from django.contrib import admin
from .models import Category, Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "active")

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
