import os
from django.core.exceptions import ValidationError


def file_size(value):
    limit = 5242880
    if value.size > limit:
        raise ValidationError('File is too large. Size should not exceed 5 MB.')
