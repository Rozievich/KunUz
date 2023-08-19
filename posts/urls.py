from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryListCreateAPIView, PostViewSet, PostListCreateView, UserViewSet, UserActiveListCreateAPIView, PostFilterApiView, PostSearchApiView

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view(), name="category"),
    path('posts/<int:pk>/change/', PostListCreateView.as_view(), name="post_change"),
    path('posts/filter/', PostFilterApiView.as_view(), name="post_filter"),
    path('posts/search/', PostSearchApiView.as_view(), name="post_search"),
    path('users/<int:pk>/change/', UserActiveListCreateAPIView.as_view(), name="users_change"),
    path('', include(router.urls))
]

