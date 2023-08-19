from rest_framework.serializers import ModelSerializer
from rest_framework.fields import HiddenField, CurrentUserDefault
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Category, Post


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostModelSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = "id", "image", "title_uz", "title_en", "title_ru", "summary_uz", "summary_en", "summary_ru", "body_uz", "body_en", "body_ru", "views", "category", "active", "created_at", "author"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = UserModelSerializer(instance.author).data['username']
        return data


class PostActiveModelSerilizer(ModelSerializer):
    class Meta:
        model = Post
        fields = "active",


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "id", "username", "first_name", "last_name", "email", "password"

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        new_password = validated_data.get('password')
        if new_password:
            instance.password = make_password(new_password)

        instance.save()
        return instance


class UserActiveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "id", "is_staff",
