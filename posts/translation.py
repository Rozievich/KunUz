from modeltranslation.translator import register, TranslationOptions
from .models import Post, Category


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'body')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
