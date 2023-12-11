from django.urls import path
from . import views

urlpatterns = [
    path('place_category/', views.place_category),  # 장소 카테고리 선택 화면으로 가기
    path('references/', views.references),  # 나들이 장소 선택 화면으로 가기
    path('afterpick/', views.afterpick),  # 선택한 장소의 정보 확인하는 화면으로 가기
]