from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('choose/', views.choose, name='choose'),
]