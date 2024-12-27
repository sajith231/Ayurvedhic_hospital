from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('doctor/', views.doctor, name='doctor'),
    path('login/', views.login_view, name='login'),
    path('gallery/', views.gallery, name='gallery'),
    path('logout/', views.logout_view, name='logout'),  # Use your custom logout view
]