from django.urls import path
from . import views


app_name = 'frontend'

urlpatterns = [
    path("", views.homepage, name="about"),
    path("classifier", views.image_classifier, name="classifier"),
    path("generator", views.image_generator, name="generator"),
    path("team", views.team, name="team")
]