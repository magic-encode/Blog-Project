from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog_detail/', views.blog_, name='blog_'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('lost-password/', views.lost_password, name='lost_password'),
]

