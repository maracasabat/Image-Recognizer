

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),


    path('photos/', views.photo_list, name='photo_list'),

    path('photos_list/', views.DataBasePhotosList.as_view(), name='photo_list'),
    path('photos/clear/', views.clear_database, name='clear_database'),
    path('photos/<int:pk>/', views.delete_photo, name='delete_photo'),

    path('photos_upload_cifar10/', views.BasicUploadViewCifar10.as_view(), name='photo_upload_cifar10'),
    path('photos_upload_cifar100/', views.BasicUploadViewCifar100.as_view(), name='photo_upload_cifar100'),
    path('basicphoto/upload/', views.BasicUploadView.as_view(), name='basic_upload'),
    path('predict_cifar10_dropdown/<int:pk>/', views.predict_cifar10_dropdown, name='predict_cifar10_dropdown'),
    path('predict_cifar100_dropdown/<int:pk>/', views.predict_cifar100_dropdown, name='predict_cifar100_dropdown'),
]
