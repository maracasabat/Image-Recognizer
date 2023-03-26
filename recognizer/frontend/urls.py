from django.urls import path
from . import views


app_name = 'frontend'

urlpatterns = [
    path("", views.homepage, name="about"),
    path("classifier", views.image_classifier, name="classifier"),
    path("gallery", views.gallery_page, name="gallery"),
    path("team", views.team, name="team"),
    path('switch_theme', views.change_theme, name='change-theme'),
    # path('predict/', views.predict_pictures, name='predict_pictures'),
]