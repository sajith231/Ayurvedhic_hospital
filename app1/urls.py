from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
     
     
      ]
