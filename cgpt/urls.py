
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_keyword, name='recommend_keyword'),
]