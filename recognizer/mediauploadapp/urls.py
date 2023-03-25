

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('files/', views.file_list, name='file_list'),
    path('files/image', views.file_list_image, name='file_list_image'),
    path('files/video', views.file_list_video, name='file_list_video'),
    path('files/document', views.file_list_document, name='file_list_document'),
    path('files/music', views.file_list_music, name='file_list_music'),
    path('files/other', views.file_list_other, name='file_list_other'),

    path('files/upload/', views.upload_file, name='upload_file'),
    path('files/<int:pk>/', views.delete_file, name='delete_file'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),

    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

    path('photos_cifar10/', views.photo_list, name='photo_list_cifar10'),
    path('photos_cifar100/', views.photo_list, name='photo_list_cifar100'),
    path('photos_chat_gpt/', views.photo_list, name='photo_list_chat_gpt'),
    path('photos_image_generator/', views.photo_list, name='photo_list_image_generator'),

    path('photos_list/', views.DataBasePhotosList.as_view(), name='photo_list'),
    path('photos/clear/', views.clear_database, name='clear_database'),
    path('photos/<int:pk>/', views.delete_photo, name='delete_photo'),

    path('photos_upload_cifar10/', views.BasicUploadViewCifar10.as_view(), name='photo_upload_cifar10'),
    path('photos_upload_cifar100/', views.BasicUploadViewCifar100.as_view(), name='photo_upload_cifar100'),
    path('basicphoto/upload/', views.BasicUploadView.as_view(), name='basic_upload'),
    path('predict_cifar10_dropdown/<int:pk>/', views.predict_cifar10_dropdown, name='predict_cifar10_dropdown'),
    path('predict_cifar100_dropdown/<int:pk>/', views.predict_cifar100_dropdown, name='predict_cifar100_dropdown'),
    path('predict/', views.predict_pictures, name='predict_pictures'),
]
