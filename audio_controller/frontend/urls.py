from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index),
    path('join', index),
    path('create', index),
    path('join/1', index),
]