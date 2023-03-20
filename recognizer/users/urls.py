from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_view, name='register'),
    path('login', views.custom_login, name='login'),
    path('logout', views.custom_logout, name='logout'),
    path('settings/<username>', views.custom_settings, name='settings'),
    path('social/signup/', views.signup_redirect, name='signup_redirect'),
]
