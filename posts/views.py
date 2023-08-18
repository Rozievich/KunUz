from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from django_filters import rest_framework as filters
from django.contrib.auth.models import User

from .serializers import CategoryModelSerializer, PostModelSerializer, PostActiveModelSerilizer, UserModelSerializer, UserActiveSerializer
from .permissions import CategoryPermission, PostPermission, IsSuperuser, UserPermission
from .models import Category, Post
from .filters import PostSearchFilter

class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
    permission_classes = (CategoryPermission, )
    


class PostViewSet(ModelViewSet):
    serializer_class = PostModelSerializer
    queryset = Post.objects.filter(active=True)
    permission_classes = (PostPermission, )
    parser_classes = [MultiPartParser]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.method in SAFE_METHODS:
            instance.views += 1
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

class PostListCreateView(UpdateAPIView):
    serializer_class = PostActiveModelSerilizer
    queryset = Post.objects.all()
    permission_classes = (IsSuperuser, )
    http_method_names = ('patch', )


class PostFilterApiView(ListAPIView):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('category', )


class PostSearchApiView(ListAPIView):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostSearchFilter


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    permission_classes = (UserPermission, )


class UserActiveListCreateAPIView(UpdateAPIView):
    serializer_class = UserActiveSerializer
    queryset = User.objects.all()
    permission_classes = (IsSuperuser, )
    http_method_names = ("patch", )