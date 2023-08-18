from django_filters import rest_framework as filters
from .models import Post


class PostFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name="category", lookup_expr="exact")
    class Meta:
        model = Post
        fields = "category", 


class PostSearchFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains",)
    class Meta:
        model = Post
        fields = "title", 