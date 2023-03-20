from django.contrib import admin
from .models import File, Book, Photo

# Register your models here.

admin.site.register(File)
admin.site.register(Book)
admin.site.register(Photo)
# class DocumentAdmin(admin.ModelAdmin):
#     list_display = ('doc_name',)
#
# admin.site.register(Document, DocumentAdmin)