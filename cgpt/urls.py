
from django.urls import path
from . import views


app_name = 'cgpt'

urlpatterns = [
    path('', views.cgpt, name='cgpt'),
    path('recommend_keyword/', views.recommend_keyword, name='recommend_keyword'),
]