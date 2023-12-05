from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('place_category/', views.place_category),
    path('references/', views.references),
    path('afterpick/', views.afterpick),
]