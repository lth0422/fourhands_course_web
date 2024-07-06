
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend_keyword/', views.recommend_keyword, name='recommend_keyword'),
]