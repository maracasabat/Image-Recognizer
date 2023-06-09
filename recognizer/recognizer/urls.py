from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from dropzone.views import DropzoneView, file_upload_view

urlpatterns = [
    path('', include('users.urls')),
    path('', include('frontend.urls')),
    path(' ', include('mediauploadapp.urls')),
    path('admin/', admin.site.urls),
    path('__reload__/', include('django_browser_reload.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include("allauth.urls")),
    path('', DropzoneView.as_view),
    path('upload/', file_upload_view, name='upload-view')
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
