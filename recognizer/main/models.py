from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField


class PostCategory(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    slug = models.SlugField("Category slug", null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-published']


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    post_slug = models.SlugField("Post slug", null=False, blank=False, unique=True)
    content = HTMLField(blank=True, default="")
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    category = models.ForeignKey(PostCategory, default="", verbose_name="Categories", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.post_slug

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-published']
