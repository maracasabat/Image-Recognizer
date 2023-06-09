# Generated by Django 4.1.7 on 2023-03-27 17:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediauploadapp', '0003_remove_photo_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='author_id',
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(unique=True, upload_to='photos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'svg', 'jpeg', 'gif', 'eps', 'raw'])]),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
