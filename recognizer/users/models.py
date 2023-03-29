import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Users', self.username, instance)
        return None

    STATUS = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = HTMLField("Description", max_length=600, default='', blank=True)
    first_name = models.CharField("First Name", max_length=100, default='', blank=True)
    last_name = models.CharField("Last Name", max_length=100, default='', blank=True)
    avatar = models.ImageField(upload_to=image_upload_to, blank=True, null=True, default='default/avatar.webp')

    def __str__(self):
        return self.username