from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
import cloudinary.uploader


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.ImageField(upload_to='photos/',
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['jpg', 'png', 'svg', 'jpeg', 'gif', 'eps', 'raw'])],
                             unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
