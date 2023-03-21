from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("phonebook", views.phonebook_page, name="phonebook"),
    path("notebook", views.notebook_page, name="notebook"),
    path("gallery", views.gallery_page, name="gallery"),

]