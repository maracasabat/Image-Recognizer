import os
from django.core.exceptions import ValidationError


def file_size(value):
    limit = 5242880
    if value.size > limit:
        raise ValidationError('File is too large. Size should not exceed 5 MB.')


def book_size(value):
    limit = 1048576
    if value.size > limit:
        raise ValidationError('File is too large. Size should not exceed 1 MB.')


def book_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext in valid_extensions:
        raise ValidationError('Unsupported file type. Only Pdf and MsWord files are allowed.')
