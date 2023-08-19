from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name=_("title_category"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)
    title = models.CharField(max_length=128, verbose_name=_('title_post'))
    summary = models.CharField(max_length=350)
    body = models.TextField()
    category = models.ManyToManyField(Category, related_name="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    @property
    def image_url(self):
        try:
            return self.image.url
        except ValueError:
            return "https://storage.kun.uz/source/thumbnails/_medium/9/-s_RNFKgzfyXrRpnqL6puF3vnKf68uF-_medium.jpg"

    def __str__(self) -> str:
        return self.title
