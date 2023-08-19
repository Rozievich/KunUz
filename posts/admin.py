from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Post, Category


@admin.register(Post)
class PostModelAdmin(TranslationAdmin):
    list_display = ('title_uz', 'active')


@admin.register(Category)
class CategoryModelAdmin(TranslationAdmin):
    list_display = ('title', 'title_en', 'title_ru')
