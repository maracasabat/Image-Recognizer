from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import FileExtensionValidator
from django.contrib.auth import get_user_model
from .filechecker import file_size


# Create your models here.


class File(models.Model):
    CATEGORY = (
        ('video', ('Video')),
        ('image', ('Image')),
        ('document', ('Document')),
        ('music', ('Music')),
        ('other', ('Other')),
    )
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    category = models.CharField('File Category', max_length=40, choices=CATEGORY, default='other')
    publication_date = models.DateTimeField(default=now, blank=True)
    author_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    publication_date = models.DateTimeField(default=now, blank=True)
    author_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/',
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'svg', 'jpeg'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
