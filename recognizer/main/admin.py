from django.contrib import admin
from .models import Post, PostCategory


class PostCategoryAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'slug',
        # 'published'
    ]


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {"fields": ['title', 'subtitle', 'post_slug', 'category']}),
        ("Content", {"fields": ['content']}),
        ("Date", {"fields": ['modified']})
    ]


# Register your models here.
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
