from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('films/', views.film_list, name='films'),
    path('film/detail/<int:pk>', views.film_detail, name='film_detail'),
]
