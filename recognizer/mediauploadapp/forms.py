# -*- coding: utf-8 -*-
from django import forms
from .models import Photo
from .filechecker import file_size


class PhotoForm(forms.ModelForm):
    file = forms.FileField(required=True, validators=[file_size])
    class Meta:
        model = Photo
        fields = ('file', )