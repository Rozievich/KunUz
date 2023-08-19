from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Post

class PostTranslationAdmin(TranslationAdmin):
    pass
admin.register(Post, PostTranslationAdmin)

# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ("title", "author", "active")

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
